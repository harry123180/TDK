import math
import numpy as np
import cv2
import time
import random
# 建立一張 512x512 的 RGB 圖片（黑色）
pi = math.pi
diameter = 113
x = 0
y = 0
cx = []
cy = []
theda = 0
ti =0
while(True):
    ti+=1
    img = np.zeros((1000, 1000, 3), np.uint8)
    if (ti<100):
        Nr = 60#random.randint(-80, 100) RPM
        Nl = 60#random.randint(-80, 100) RPM
    elif(ti >100 and ti < 400):
        Nr = 10
        Nl = 60
    elif(ti>400 and ti < 600):
        Nr = 60
        Nl =  10
    else:
        Nr = 60
        Nl = 60

    nr = Nr / 60
    nl = Nl / 60
    vr = nr * pi * diameter
    vl = nl * pi * diameter
    t = 0.01  # 10ms
    l = 230
    #ti = 0
    v = (vr + vl) / 2
    omega = (vl - vr) / (2 * l)

    # 將圖片用淺灰色 (200, 200, 200) 填滿
    img.fill(200)
    r = math.radians(theda)
    x = x+t*v*math.cos(theda)
    y = y+t*v*math.sin(theda)
    theda = theda+omega*t
    print("x = ",x,"y= ",y)
    cx.append(int(x/10))
    cy.append(int(y/10))
    #print(math.cot(0))
    # 在圖片上畫一條紅色的對角線，寬度為 5 px

    if(ti%10==0):
        cv2.putText(img, str(ti), (10, 140), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 255), 1, cv2.LINE_AA)
        for o in range(len(cx)):
            cv2.circle(img,(cx[o]+500, cy[o]+500), 5, (255, 0, 0), -1)
        cv2.imshow('My Image', img)
    time.sleep(0.01)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    # 顯示圖片
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)





