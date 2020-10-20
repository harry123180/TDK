import serial
import numpy as np
import matplotlib.pyplot as plt
import threading
import time
s1= serial.Serial('COM8',115200)
plt.axis([0, 10, 0, 1])

def hextodex(alist):
    a2 = alist[0]
    a1 = alist[1]

    if (a2 < 0):
        dd = (256 * a2 + a1) + 256
    elif (a2 >= 0):
        dd = 256 * a2 + a1

    return dd
def hextodex4(alist):
    a4 = alist[0]
    a3 = alist[1]
    a2 = alist[2]
    a1 = alist[3]
    #print('a1=',a1)
    rr2 = 256 * a2 + a1
    rr1 = 65536 * a3 + rr2
    if (a4 != 255):
        dd = 16777216 * a4 + rr1
    elif(a4 ==255):
        dd = 16777216*a4+rr1 - 4294967295

    return dd



def motor_v(N,spd,packet):
    if(spd<0):
        spd = 65535+spd
    spd2 = spd // 256
    spd1 = spd % 256
    packet.append(0xaa)
    packet.append(0x01)
    packet.append(N)
    packet.append(spd2)
    packet.append(spd1)
    packet.append(0x00)
    packet.append(0x00)
    packet.append(0x0a)
    packet.append(0x28)
    packet.append(0xee)  ##END

for i in range(150):
    packet = bytearray()
    motor_v(0x01,i,packet)
    s1.write(packet)
    packet = bytearray()
    motor_v(0x02,i,packet)
    s1.write(packet)
    time.sleep(0.1)
time.sleep(3)
for i in range(150):
    packet = bytearray()
    motor_v(0x01, 150-i, packet)
    s1.write(packet)
    packet = bytearray()
    motor_v(0x02, 150-i, packet)
    s1.write(packet)
    time.sleep(0.01)
    #print(packet)
for _ in range(10):
    packet = bytearray()
    motor_v(0x01, 0, packet)
    s1.write(packet)
    packet = bytearray()
    motor_v(0x02, 0, packet)
    s1.write(packet)
two_wheel_vlocity=[0,0]
speed = [0,0]
pos = [0,0]

while True:
    msg=[]
    new = []

    if (s1.readline(1) == b'\xee'):

        for j in range(9):
            msg.append(s1.readline(1))
        position= [int.from_bytes(msg[3], byteorder='big', signed=False),
               int.from_bytes(msg[4], byteorder='big', signed=False),
               int.from_bytes(msg[5], byteorder='big', signed=False),
               int.from_bytes(msg[6], byteorder='big', signed=False)
               ]
        vlocity = [int.from_bytes(msg[3], byteorder='big', signed=False),
               int.from_bytes(msg[4], byteorder='big', signed=False)
               ]
        #print('aaaa',new[3])
        if (msg[2]==b'\x02'):
            speed[1] =hextodex(vlocity)# (hextodex4(position))
            pos[1] = hextodex4(position)
            #print(new)
        elif(msg[2]==b'\x01'):
            speed[0] = hextodex(vlocity)#(hextodex4(position))
            pos[0] = hextodex4(position)
        print(two_wheel_vlocity)
        #print(pos)

