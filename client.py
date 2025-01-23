import socket

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 1234))

    client.send('Hello from client'.encode())
    print("Message sent to the server.")

    print("Server response:", client.recv(1024).decode())

except KeyboardInterrupt:
    print("\nProgram interrupted by the user. Closing the connection.")

finally:
    client.close()
    print("Socket closed. Exiting...")
