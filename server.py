import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Server create
server.bind(('0.0.0.0', 1234))

server.listen(5)

while True:
    client, addr = server.accept()
    print(client.recv(1024).decode())
    client.send('Hello from Server'.encode())