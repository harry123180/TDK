import socket

TCP_IP = '172.20.10.2' # this IP of my pc. When I want raspberry pi 2`s as a client, I replace it with its IP '169.254.54.195'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "100"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send((MESSAGE).encode())
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)