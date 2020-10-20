import socket
import time
ClientSocket = socket.socket()
host = '25.7.170.68'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    Input = 'a'
    Input = '0' + str(' ') + Input
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))
    time.sleep(0.02)
ClientSocket.close()