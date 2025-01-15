import socket

HOST = '127.0.0.1'
PORT = 1234

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("Connected to server")
except OSError as msg:
    print(f"Error: {msg}")
    exit(1)

with s:
    while True:
        message_to_send = input("You (Client): ")
        s.send((message_to_send + "\n").encode())

        data = s.recv(1024) 
        if not data:
            print("Connection closed by server")
            break

        message_received = data.decode().strip()
        print(f"Server: {message_received}")

print("Client finished")