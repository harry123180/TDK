import threading
import time
import serial
import random
s1 = serial.Serial('COM3', 9600)
sensor =0
a = True
action_list = ['forward','back','right','left']
spd= [1000,1000,1000,1000]
cnt = 0
Now_action = action_list[cnt]
finish = False
target = 10#cm
def infiniteloop1():
    global a,sensor,spd
    while (a):
        #print(Now_action)
        while s1.in_waiting:
            mcu_feedback = s1.readline()#.decode()  # 接收回應訊息並解碼
            #print('控制板回應0：', mcu_feedback)
            sensor = int(mcu_feedback)


        if(sensor -target >0 ):
            spd[1] = 1000+(sensor-target)*10
            spd[2] = 1000+(sensor-target)*10
            #print('++++++++++++++',sensor)
        elif(sensor-target <0):
            spd[1] = 1000+(sensor-target)*10
            spd[2] = 1000+(sensor-target)*10

            #print('-------',sensor)
        #time.sleep(0.1)

def infiniteloop2():
    global a , cnt,Now_action,finish,spd
    while (a):
        #print(spd)
        print(cnt, Now_action,spd)
        if (finish ==True):
            print('compelete')
            cnt +=1
            Now_action=action_list[cnt]
            if(finish == True and cnt ==3):
                a = False
            finish = False
        time.sleep(0.1)
def loop3():
    global finish,cnt,a #完成狀態
    while(a):
        if(cnt==0):
            time.sleep(5)
            finish=True
        elif(cnt==1):
            print('cnt == 2 is do it ')
            time.sleep(1)
            #print('do')
            finish=True
        elif(cnt==2):
            time.sleep(1)
            finish=True
        elif(cnt==3):
            time.sleep(1)
            finish=True
        time.sleep(0.1)


thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()
thread3 = threading.Thread(target=loop3)
thread3.start()