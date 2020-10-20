import serial
from time import sleep
import tkinter as tk
import threading
window = tk.Tk()
window.title('my window')
window.geometry('200x1000')
var = tk.StringVar()
l = tk.Label(window,bg='yellow',width = 20,text='empty')
l.pack()
run_state = True
runtime=0.5
#目標 傳送6個軸的角度值(0~180)至Arduino 接收
#採用10碼 開始碼為0xff 結束碼為0xee
#給定6個數字 送過去Arduino
COM_PORT = 'COM4'  # 請自行修改序列埠名稱
BAUD_RATES = 38400
ser = serial.Serial(COM_PORT, BAUD_RATES)
d=[110,90,90,90,90,90]#初始角度
msg = [0xff,0,0,0,0,0,0,0xee]#傳送訊息的陣列
def send_deg(d):
    a=[d[0],d[1],d[2],d[3],d[4],d[5]]
    for i in range(6):
        msg[i+1] = bytes([a[i]])
    msg[0] = bytes([255])
    msg[7] = bytes([238])
    #print(a)
    for i1 in range(8):
        ser.write(msg[i1])
    sleep(runtime)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
    print(a)

    while ser.in_waiting:
        mcu_feedback = ser.readline()#.decode()  # 接收回應訊息並解碼
        print('控制板回應：', mcu_feedback)



s1= tk.Scale(window,label = 'join1 ',from_=0,to=180,
             orient = tk.HORIZONTAL,length = 200)
s1.set(110)

s1.pack()
s2= tk.Scale(window,label = 'join2 ',from_=0,to=180,
             orient = tk.HORIZONTAL,length = 200)

s2.set(90)
s2.pack()
s3= tk.Scale(window,label = 'join3 ',from_=0,to=180,
             orient = tk.HORIZONTAL,length = 200)

s3.set(90)
s3.pack()
s4= tk.Scale(window,label = 'join4 ',from_=0,to=180,
             orient = tk.HORIZONTAL,length = 200)

s4.set(90)
s4.pack()
s5= tk.Scale(window,label = 'join5 ',from_=0,to=180,
             orient = tk.HORIZONTAL,length = 200)

s5.set(90)
s5.pack()
s6= tk.Scale(window,label = 'join6 ',from_=0,to=180,
             orient = tk.HORIZONTAL,length = 200)
s6.set(90)
s6.pack()
def send():
    global d
    global run_state
    print(d)
    while(True):
        d = [int(s1.get()), int(s2.get()), int(s3.get()), int(s4.get()), int(s5.get()), int(s6.get())]
        send_deg(d)
        sleep(0.5)
        if (run_state ==False ):
            break

def off():
    global run_state
    run_state = False
bt = tk.Button(window,text = 'hit me ',width = 15,
               height = 2 , command = off)

bt.pack()
t = threading.Thread(target = send)

# 執行該子執行緒
t.start()
window.mainloop()
t.join()
print('done')










