import socket
import threading

HOST = '127.0.0.1'
PORT = 12342

def send_message_function(client_socket):
    while True:
        message = input("")
        client_socket.send(message.encode())

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    # Sending the nickname
    nickname = input("Enter your nickname: ")
    s.send(nickname.encode())

    # Start a thread for sending messages
    send_thread = threading.Thread(target=send_message_function, args=(s,))
    send_thread.start()

    # Main loop to receive messages
    while True:
        try:
            message_received = s.recv(1024).decode()
            print(message_received)  # Display the message with the sender's nickname
        except:
            print("Disconnected from server")
            break
