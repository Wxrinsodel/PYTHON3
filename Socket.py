import socket
 
HOST = 'test.net'
PORT = 80


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
 
#  client COnnect to server
    s.connect((HOST, PORT))
# Send to server
    s.sendall(b'GET / HTTP/ 1.0\r\nHOST: test.net\r\n\r\n')
 
# recieve the datat from server
    data = s.recv(1024)
print('received:', repr(data))

