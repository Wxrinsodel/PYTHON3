import socket
import sys
from pyexpat.errors import messages

HOST = '0.0.0.0'
PORT = 1234

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print("Socket created")
    print("Socket bound and listening")
except OSError as msg:
    s = None
    print(f"Error creating socket: {msg}")
    exit(1)

conn, addr = s.accept()
print('Connection accepted from ', addr)

with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            print("Connection closed by client")
            break

        message_received = data.decode().strip()
        print(f"Client: {message_received}")

        message_to_send = input("You (Server): ")
        conn.send((message_to_send + "\n").encode())

s.close()
