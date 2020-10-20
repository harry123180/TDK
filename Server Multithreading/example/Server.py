import socket
import os
from _thread import *
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Waitiing for a Connection..')
ServerSocket.listen(5)
def who(number):
    if(number==0):
        a = '1'
    elif(number==1):
        a = '2'
    elif(number==2):
        a = '3'
    elif(number==4):
        a = '4'
    return a
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = str(connection.recv(2048), encoding='utf-8')
        sult = data.split(' ', 1)

        reply = 'Server Says: YOU ARE ' + sult[1]+who(int(sult[0]))#.encode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()