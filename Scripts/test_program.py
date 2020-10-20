import serial
from time import sleep
import sys
import numpy as np

COM_PORT = 'COM5'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES)
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
    spd2 = spd // 256
    spd1 = spd % 256
    mot4, mot3, mot2, mot1 = ItoHex(pls)
    if (mot4 < 0): mot4 = mot4 + 256
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
O=0
while (choice != 's'):
    # 接收用戶的輸入值並轉成小寫
    choice = input('按s開始............  ').lower()

try:
    while (O==0):
        packet = bytearray()
        motor_move(0x01, pls1, spd1)
        motor_move(0x02, pls2, spd2)
        motor_move(0x03, pls3, spd3)
        motor_move(0x04, pls4, spd4)
        ser.write(packet)
        print(ser.readline())


        # print(len(packet))
        #       print('\nindx_ccw, indx_cw = %d  %d' %(indx_ccw, indx_cw))
        O+=1
        '''
        while ser.in_waiting:
            mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
            print('控制板回應：', mcu_feedback)
        '''
        sleep(2.4)

except KeyboardInterrupt:
    ser.close()
    print('再見！')