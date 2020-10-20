import math
#import serial
from time import sleep
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
var = tk.StringVar()
l = tk.Label(window,bg='yellow',width = 20,text='empty')
l.pack()

#COM_PORT = '/dev/ttyUSB0'  # 請自行修改序列埠名稱
#BAUD_RATES = 115200
#ser = serial.Serial(COM_PORT, BAUD_RATES)
pos_list = []
diameter = 15.24
fac = 4896 / (diameter * math.pi)


def ItoHex(d):
    m4 = d // 16777216  # 取商數
    r1 = d % 16777216  # 取餘數
    m3 = r1 // 65536  # 取商數
    r2 = r1 % 65536  # 取餘數
    m2 = r2 // 256  # 取商數
    m1 = r2 % 256  # 取餘數
    return m4, m3, m2, m1


def hextodex(alist):
    a4 = alist[0]
    a3 = alist[1]
    a2 = alist[2]
    a1 = alist[3]
    rr2 = 256 * a2 + a1
    rr1 = 65536 * a3 + rr2
    dd = 16777216 * a4 + rr1
    if (dd < 0):
        dd = dd + 16843008
    return dd


def dist_est(dist):
    pulse = int(dist * fac)
    return pulse


choice = ''
condition = True
O = 0
cnt = 1
k = 1
dly = 2
dly1 = dly
packet = bytearray()


def velocity_move(spd, N, pac):
    # mot4,mot3,mot2,mot1 = ItoHex(pls)
    if (spd < 0): spd = 65535 + spd
    spd2 = spd // 256
    spd1 = spd % 256
    # mot4, mot3, mot2, mot1 = ItoHex(pls)
    # if (mot4 < 0): mot4 = mot4 + 256
    pac.append(0xaa)  ##開始
    pac.append(0x01)  ##模式
    pac.append(N)  ##幾號機
    pac.append(spd2)  # RPM上限定義
    pac.append(spd1)  # RPM上限定義
    pac.append(0x00)  # 脈衝數定義
    pac.append(0x00)
    pac.append(0x00)
    pac.append(0x00)  # 脈衝數定義
    pac.append(0xee)  ##END
    #ser.write(pac)


#    packet.append(0xEE)  #END
def velocity_output(v_list, t_list):
    for t in range(len(t_list)):
        pac = bytearray()
        velocity_move(-v_list[t], 0x01, pac)
        pac = bytearray()
        velocity_move(v_list[t], 0x02, pac)
        pac = bytearray()
        velocity_move(v_list[t], 0x03, pac)
        pac = bytearray()
        velocity_move(-v_list[t], 0x04, pac)
        print(v_list)

        sleep(t_list[t])


packet = bytearray()
velocity_list = [   0   ,   0   ,   0   ,   0   ]
def print_selection(v):
    l.config(text = 'you have selected'+v)
    for i in range(4):
        velocity_list[i] = v
    print(velocity_list)
    velocity_output(velocity_list,1)



s = tk.Scale(window,label = 'try me ',from_=0,to=10000,
             orient = tk.HORIZONTAL,length = 200,
             showvalue = 0,tickinterval=1,resolution=100,
             command = print_selection)


s.pack()




window.mainloop()