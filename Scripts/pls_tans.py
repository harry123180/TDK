def ItoHex(d):
    m4 = d // 16777216  # 取商數
    r1 = d % 16777216  # 取餘數
    print('r1=',r1)
    m3 = r1 // 65536  # 取商數
    r2 = r1 % 65536  # 取餘數
    print('r2=',r2)
    m2 = r2 // 256  # 取商數
    m1 = r2 % 256  # 取餘數

    return m4, m3, m2, m1
a4,a3,a2,a1=ItoHex(4896*3)
#print(a4,a3,a2,a1)
rr2 = 256*a2+a1
#print('rr2=',rr2)
rr1 = 65536*a3+rr2
dd= 16777216*a4+rr1
#print('rr1=',rr1)
#print('dd=',dd)
#print(4896*3)

print(ItoHex(0x7d0))
def hextodex(list):
    a4 = list[0]
    a3 = list[1]
    a2 = list[2]
    a1 = list[3]
    rr2 = 256*a2+a1
    rr1 = 65536*a3+rr2
    dd= 16777216*a4+rr1
    return dd

def motor_move(pls,spd,N):
    mot4,mot3,mot2,mot1 = ItoHex(pls)
    if (spd<0): spd=65535+spd
    spd2 = spd//256        #取商數
    spd1 = spd%256         #取餘數

    packet.append(0x00)    #保留位元
    packet.append(0x0+N)  #0x40表示位置模式, N:ID號碼
    packet.append(0xAA)    #電流上限定義(此處不用)
    packet.append(0xAA)    #電流上限定義(此處不用)
    packet.append(spd2)    #RPM上限定義
    packet.append(spd1)    #RPM上限定義
    if (mot4 < 0): mot4 = mot4 + 256
    packet.append(mot4)    #脈衝數(由高到低位元組)
    packet.append(mot3)
    packet.append(mot2)
    packet.append(mot1)  #脈衝數定義
#    packet.append(0xEE)  #END
packet = bytearray()

motor_move(-2000,-3000,3)
print(packet)
#def velocity_move(spd,N):
a = bytearray()
b = bytearray()
J=(65535-3000)
J1=J//256
J2=J%256
#print(type(J1))
a.append(J1)
b.append(47)
print(a)
print(b)
#print(hex(J2))