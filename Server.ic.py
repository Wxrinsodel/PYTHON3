import socket
import threading

HOST = '127.0.0.1'
PORT = 12342

clients = []
nicknames = []

# Function to broadcast messages to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle messages from a client
def handle(client):
    while True:
        try:
            # Receive the message from the client
            message = client.recv(1024).decode()
            if not message:
                break
            index = clients.index(client)
            nickname = nicknames[index]
            # Prepend the sender's nickname to the message
            formatted_message = f"{nickname}: {message}"
            broadcast(formatted_message.encode())
        except:
            # Remove the client and notify others on error
            index = clients.index(client)
            nickname = nicknames[index]
            clients.remove(client)
            client.close()
            nicknames.remove(nickname)
            broadcast(f"{nickname} has left the chat!\n".encode())
            break

# Function to accept and manage new clients
def receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server started on {HOST}:{PORT}")

        while True:
            client, address = server.accept()
            print(f"Connected with {str(address)}")

            # Request and store the nickname
            client.send("NICK".encode())
            nickname = client.recv(1024).decode()
            nicknames.append(nickname)
            clients.append(client)

            print(f"Nickname is {nickname}")
            broadcast(f"{nickname} has joined the chat!\n".encode())
            client.send("Connected to the server!\n".encode())

            # Start a new thread for handling the client
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

if __name__ == "__main__":
    receive()
