import socket
import os
import threading
import numpy as np
import time
import matplotlib.pyplot as plt

HOST = '25.16.249.17'
PORT = 8000
plt.axis([0, 1000, 0, 1])
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
cX =0
cY=0
runtime = 1000 #運行時間 180秒
program_run_state = True
def server_job():
    while True:
        global cX
        global cY
        #print("has be run")
        conn, addr = server.accept()
        try:
            clientMessage = str(conn.recv(1024), encoding='utf-8')
            d = clientMessage.split(' ', 1)
            cX=int(d[0])
            cY=int(d[1])
            print('Client message is:', d)
        #print(int(clientMessage))
        except:
            print("notthing")
        if(program_run_state==True):
            serverMessage = '1'
        if(program_run_state==False):
            serverMessage = '0'
        conn.sendall(serverMessage.encode())
        conn.close()

def car_control():
    if(cX<240):
        print("向左")
    elif(cX>240):
        print("向右")
def sim_car_control():
    n=0
    while(True):
        car_control()
        n+=1
        time.sleep(0.1)
        if(program_run_state==0):
            print("end!")
            break
def time_job():
    global program_run_state
    time.sleep(runtime)
    program_run_state=False
def reader():
    now_time = 0
    #os.system("python client.py")
    while(program_run_state):
        now_time+=1
        time.sleep(1)
        if(now_time %10 ==0):
            print("現在時間",now_time)


"""
def draw():
    i=0
    x = list()
    y = list()
    z = list()
    while i < 1000:
        temp_y = np.random.random()
        x.append(i)
        y.append(cX)
        plt.scatter(i, cX)
        plt.pause(0.05)
        i += 1
    plt.show()
"""
t = threading.Thread(target = server_job)
t2 = threading.Thread(target = sim_car_control)
timer = threading.Thread(target = time_job)
Reader = threading.Thread(target=reader)
#t2 = threading.Thread(target = draw)
# 執行他
t.start()
t2.start()
timer.start()
Reader.start()
#os.system("python client.py")
#t2.start()
t.join()
t2.join()
timer.start()
Reader.join()
