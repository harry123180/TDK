import socket
import random
import time
HOST = '127.0.0.1'
PORT = 8000

a = 14
b = 14
c = str(a)+str(' ')+str(b)
#print(c)
d = c.split(' ', 1 )
#print(type(d))
clientMessage = c
i = 0

while (True):
    i+=1
    cX= random.randint(1,480)
    cY = random.randint(1,640)
    randomt = random.randint(1,20)
    c = str(cX) + str(' ') + str(cY)
    clientMessage = c
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.sendall(clientMessage.encode())

    serverMessage = str(client.recv(1024), encoding='utf-8')

    print('Server:', serverMessage)

    time.sleep(randomt/100)
    if (int(serverMessage)==0):
        break

client.close()