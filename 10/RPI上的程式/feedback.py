import math
import threading
import serial
import socket
from time import sleep

COM_PORT = '/dev/ttyUSB0'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES)
global packet
pls_nowr = 0
pls_nowl = 0
global spd
pos1_ = 0
pos2_ = 0
#####################################IP set######

ClientSocket = socket.socket()
host = '25.7.170.68'
port = 1233
c = 0


def hextodex(alist):
    a4 = alist[0]
    a3 = alist[1]
    a2 = alist[2]
    a1 = alist[3]
    # print(alist)
    rr2 = 256 * a2 + a1
    rr1 = 65536 * a3 + rr2
    dd = 16777216 * a4 + rr1
    if (dd > 2147483647):
        dd = dd - pow(2, 32)
    return dd


def reset():
    for i in range(5):
        packet = bytearray()
        packet.append(0xaa)  ##開始
        packet.append(0x00)  ##模式
        packet.append(0x00)  ##幾號機
        packet.append(0x00)  # RPM上限定義
        packet.append(0x00)  # RPM上限定義
        packet.append(0x00)  # 脈衝數定義
        packet.append(0x00)
        packet.append(0x00)
        packet.append(0x00)  # 脈衝數定義
        packet.append(0xee)
        ser.write(packet)


def set_spd_mode():
    for i in range(5):
        packet = bytearray()
        packet.append(0xaa)  ##開始
        packet.append(0x02)  ##模式
        packet.append(0x01)  ##幾號機
        packet.append(0x00)  # RPM上限定義
        packet.append(0x00)  # RPM上限定義
        packet.append(0x00)  # 脈衝數定義
        packet.append(0x00)
        packet.append(0x00)
        packet.append(0x00)  # 脈衝數定義
        packet.append(0xee)
        ser.write(packet)
        packet = bytearray()
        packet.append(0xaa)  ##開始
        packet.append(0x02)  ##模式
        packet.append(0x02)  ##幾號機
        packet.append(0x00)  # RPM上限定義
        packet.append(0x00)  # RPM上限定義
        packet.append(0x00)  # 脈衝數定義
        packet.append(0x00)
        packet.append(0x00)
        packet.append(0x00)  # 脈衝數定義
        packet.append(0xee)
        ser.write(packet)


try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)


def send(p1, p2):
    # Input = input('Say Something: ')
    Input = '1' + str(' ') + str(p1) + str(' ') + str(p2)
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    # print(Response.decode('utf-8'))


def loop():
    global pos1_
    global pos2_
    while (True):
        send(pos1_, pos2_)


def read_job():
    global pos1_
    global pos2_
    if (ser.readline(1) == b'\xee'):
        msg = []
        for j in range(9):
            msg.append(ser.readline(1))
            # new = [int(msg[3]),msg[4],msg[5],msg[6]]
        new2 = [msg[3], msg[4], msg[5], msg[6]]
        new = [int.from_bytes(msg[3], byteorder='big', signed=False),
               int.from_bytes(msg[4], byteorder='big', signed=False),
               int.from_bytes(msg[5], byteorder='big', signed=False),
               int.from_bytes(msg[6], byteorder='big', signed=False)]
        # print(msg)
        # t_pos = hextodex(new)
        if (msg[2] == b'\x01'):
            pos1_ = hextodex(new)
        elif (msg[2] == b'\x02'):
            pos2_ = hextodex(new)
    # send(pos1_,pos2_)


def timer_funtion():
    while (True):
        read_job()
        # print('do')
        # sleep(0.02)


spd = 20
de = 360
reset()
sleep(5)
c = 1
if __name__ == '__main__':
    set_spd_mode()
    t = threading.Thread(target=timer_funtion)
    t2 = threading.Thread(target=loop)
    t2.start()
    t.start()
    # send()
    t.join()
    t2.join()



