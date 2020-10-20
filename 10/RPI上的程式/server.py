import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '25.7.170.68'
port = 1233
ThreadCount = 0

pls1 = 0
pls2 = 0
############################################
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


############################################
def block_number(number):
    global pls1
    global pls2
    block_num = int(number[0])
    rply = 'tt'
    if (block_num == 0):
        rply = '1' + str(' ') + str(pls1) + str(' ') + str(pls2)
    elif (block_num == 1 and len(number) == 3):
        pls1 = number[1]
        pls2 = number[2]
        print(pls1, pls2)
        rply = '2'
    elif (block_num == 2):
        rply = '3'
    elif (block_num == 3):
        rply = '4'
    elif (block_num == 4):
        rply = '5'
    elif (block_num == 5):
        rply = '6'
    elif (block_num == 6):
        rply = '7'
    return rply


##############################################
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = str(connection.recv(2048), encoding='utf-8')
        sult = data.split(' ')
        # print(sult)
        reply = block_number(sult)

        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()


while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
