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
s0 = serial.Serial('COM5', 115200)
s1 = serial.Serial('COM4', 9600)

global packet
bb = 16777216  # (65536*256)


def ItoHex(d):
    m4 = d // 16777216  # 取商數
    r1 = d % 16777216  # 取餘數
    m3 = r1 // 65536  # 取商數
    r2 = r1 % 65536  # 取餘數
    m2 = r2 // 256  # 取商數
    m1 = r2 % 256  # 取餘數

    return m4, m3, m2, m1


def motor_move(N, pls, spd):
    global packet
    spd2 = spd // 256
    spd1 = spd % 256
    mot4, mot3, mot2, mot1 = ItoHex(pls)
    if (mot4 < 0):
        mot4 = mot4 + 256
    packet.append(0xaa)  ##開始
    packet.append(0x02)  ##模式
    packet.append(N)  ##幾號機
    packet.append(spd2)  # RPM上限定義
    packet.append(spd1)  # RPM上限定義
    packet.append(mot4)  # 脈衝數定義
    packet.append(mot3)
    packet.append(mot2)
    packet.append(mot1)  # 脈衝數定義
    packet.append(0xee)  ##END


spd = 3000
spd0 = 1000
pls1 = 4896 * 3
pls2 = 4896
pls3 = 4896 * 3
pls4 = 4896
spd1 = spd
spd2 = spd0
spd3 = spd
spd4 = spd0

choice = ''
def car_I_K(speed_of_x,speed_of_y,speed_of_omega):


def open():
    global packet
#############################################
    packet = bytearray()
    motor_move(0x01, pls1, spd1)
    motor_move(0x02, pls2, spd2)
    motor_move(0x03, pls3, spd3)
    motor_move(0x04, pls4, spd4)
    s0.write(packet)

def off():
    global packet
    packet = bytearray()
    motor_move(0x01, 0, spd1)
    motor_move(0x02, 0, spd2)
    motor_move(0x03, 0, spd3)
    motor_move(0x04, 0, spd4)
    s0.write(packet)


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
        while s1.in_waiting:
            mcu_feedback = s1.readline().decode()  # 接收回應訊息並解碼
            print('控制板回應0：', mcu_feedback)


except KeyboardInterrupt:

    print('再見！')