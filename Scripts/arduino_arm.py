
import serial
from time import sleep
import sys
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x400')
var = tk.StringVar()

COM_PORT = 'COM4'  # 請自行修改序列埠名稱
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)


def one_ADD():
    print('傳送開燈指令')
    ser.write(b'ADD_A\n')  # 訊息必須是位元組類型
    sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
    while ser.in_waiting:
        mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
        print('控制板回應：', mcu_feedback)

def one_MIN():
    print('傳送開燈指令')
    ser.write(b'MIN_A\n')  # 訊息必須是位元組類型
    sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
    while ser.in_waiting:
        mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
        print('控制板回應：', mcu_feedback)

def two_ADD():
    print('傳送開燈指令')
    ser.write(b'ADD_B\n')  # 訊息必須是位元組類型
    sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
    while ser.in_waiting:
        mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
        print('控制板回應：', mcu_feedback)

def two_MIN():
    print('傳送開燈指令')
    ser.write(b'MIN_B\n')  # 訊息必須是位元組類型
    sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
    while ser.in_waiting:
        mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
        print('控制板回應：', mcu_feedback)


bt = tk.Button(window,text = '馬達一增 ',width = 15,
               height = 2 , command = one_ADD)

bt.pack()
bt1 = tk.Button(window,text = '馬達一減 ',width = 15,
               height = 2 , command = one_MIN)

bt1.pack()
bt2 = tk.Button(window,text = '馬達二增 ',width = 15,
               height = 2 , command = two_ADD)

bt2.pack()
bt3 = tk.Button(window,text = '馬達二減',width = 15,
               height = 2 , command = two_MIN)

bt3.pack()

window.mainloop()


