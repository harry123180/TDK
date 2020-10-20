import serial
import threading
import sys
from time import sleep

# 今天目標
# 實現脈衝傳輸
# 計算車體運動學分析
# 斜向走
# 雙Serial port 傳輸
"""
def serial_read(s,Variable_text):
    word = b'Variable_text\n'
    s.write(word)
    line = s.readline().decode()
    print(line)



"""
s0 = serial.Serial('COM3', 115200)
s1 = serial.Serial('COM4', 9600)


def open():
    word = b'LED_ONN\n'
    s0.write(word)
    print("do open")
    line = s0.readline().decode()
    print(line)


def off():
    word = b'LED_OFFF\n'
    s0.write(word)
    line = s0.readline().decode()
    print(line)


def read():
    while s0.in_waiting:
        mcu_feedback0 = s0.readline().decode()  # 接收回應訊息並解碼
        print('控制板回應0：', mcu_feedback0)


try:
    while True:
        # 接收用戶的輸入值並轉成小寫
        choice = input('按1開燈、按2關燈、按e關閉程式  ').lower()

        if choice == '1':
            print('傳送開燈指令')
            text = b'LED_ON\n'
            thread1 = threading.Thread(target=open)
            thread1.start()
            thread1.join()
            s1.write(text)
            sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
        elif choice == '2':
            print('傳送關燈指令')
            text = b'LED_OFF\n'
            thread2 = threading.Thread(target=off)
            thread2.start()
            thread2.join()
            s1.write(text)
            sleep(0.5)
        elif choice == 'e':
            print('再見！')
            sys.exit()
        else:
            print('指令錯誤…')
        while s0.in_waiting:
            mcu_feedback = s0.readline().decode()  # 接收回應訊息並解碼
            print('控制板回應0：', mcu_feedback)
        thread3 = threading.Thread(target=read)
        thread3.start()
        thread3.join()

except KeyboardInterrupt:

    print('再見！')