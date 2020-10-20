import cv2
import numpy as np
import math
cap = cv2.VideoCapture(0)
i = 0
num =-1
import serial
COM_PORT = 'COM4'  # 請自行修改序列埠名稱
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)

while (1):
    ret, frame = cap.read()
    num = -1
    center = frame.shape

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (13, 13), 0)
    ret, binary = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    """
    lower_hsv = np.array([100, 43, 46])
    #upper_hsv = np.array([180, 235, 46])
    upper_hsv = np.array([124, 255, 255])
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    """
    paper_low = np.array([26, 43, 46])
    paper_high = np.array([34, 255, 255])
    paper_low_2 = np.array([11, 43, 46])
    paper_high_2 = np.array([25, 255, 255])
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    curr_mask = cv2.inRange(hsv, paper_low_2, paper_high_2)
    curr_mask2 = cv2.inRange(hsv, paper_low, paper_high)
    curr_mask3 = cv2.inRange(hsv, lower_green, upper_green)
    # bitwiseOr = cv2.bitwise_or(curr_mask2,curr_mask3)
    # cv2.imshow('bitwiseOr = ',bitwiseOr)
    mask = curr_mask + curr_mask2 + curr_mask3
    #cv2.imshow("video", frame)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in range(len(contours)):
        # 提取与绘制轮廓



        # 轮廓逼近
        epsilon = 0.01 * cv2.arcLength(contours[cnt], True)
        approx = cv2.approxPolyDP(contours[cnt], epsilon, True)

        # 分析几何形状
        corners = len(approx)
        shape_type = ""
        area = cv2.contourArea(contours[cnt])
        p = cv2.arcLength(contours[cnt], True)
        r1= pow((area/math.pi),0.5)
        r2 = p / (2*math.pi)
        a = pow(pow((r1-r2),2),0.5)

        if (corners <= 6 and area > 2000):# and a ==4):
            cv2.drawContours(frame, contours, cnt, (0, 255, 0), 2)
            num = cnt

                #cv2.drawContours(frame, contours, cnt, (0, 255, 0), 2)

                # 在中心點畫上黃色實心圓
    #print(center)
    if (num != -1):
        M = cv2.moments(contours[num])
        if (M["m00"] != 0):

            cX = int(M["m10"] / M["m00"])

            cY = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cX, cY), 10, (1, 227, 254), -1)
            print(cX-320)

            if (cX - 320 >30 ):
                print ('向右')
                ser.write(b'MIN_A\n')

            if (cX - 320 <-30 ):
                print ('向左')
                ser.write(b'ADD_A\n')
            else:
                print('置中')
            if(cY - 240 >30):
                print('向下')
                ser.write(b'ADD_B\n')
            if(cY - 240 <-30):
                print('向上')
                ser.write(b'MIN_B\n')



                #cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)
    cv2.imshow("mask", mask)

    cv2.imshow("capture", frame)
    k = cv2.waitKey(1)

    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('C:\\Users\\user\\Desktop\\car_view\\' + str(i) + '.jpg', frame)
        i += 1

cap.release()
cv2.destroyAllWindows()
