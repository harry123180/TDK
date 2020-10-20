import cv2
import numpy as np
import math
distance = 570
def mask_area(image,distance):
    y_pixel = int(52.11*math.log(distance)-124.07)
    size = image.shape
    x_max=size[1]
    sss = np.zeros([480, 640], dtype=np.uint8)
    sss[y_pixel:size[1],0:x_max ] = 255
    #print("xmax = ",x_max)
    kernel_size = 3
    image_blur = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    hsv_img = cv2.cvtColor(image_blur, cv2.COLOR_BGR2HSV)
    paper_low = np.array([100, 43, 46])
    paper_high = np.array([124, 255, 255])
    curr_mask = cv2.inRange(hsv_img, paper_low, paper_high)
    mask = curr_mask
    image_masked = cv2.add(mask, np.zeros(np.shape(mask), dtype=np.uint8), mask=sss)
    return image_masked



image1 = cv2.imread('D:\\TDKsPicture\\CX0\\570cm2.jpg')

cv2.imshow('org1',image1)

img1 = mask_area(image1,400)
cv2.imshow("mask",img1)
image=cv2.add(image1, np.zeros(np.shape(image1), dtype=np.uint8), mask=img1)
# 找出所有Contours

(cnts, _) = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

i=0
j=0
#cv2.drawContours(image1, cnts, -1, (0, 255, 0), 2)
for c in cnts:
    # CV2.moments會傳回一系列的moments值，我們只要知道中點X, Y的取得方式是如下進行即可。

    M = cv2.moments(c)

    if (M["m00"]!=0):

        cX = int(M["m10"] / M["m00"])

        cY = int(M["m01"] / M["m00"])
        area = cv2.contourArea(c)  # 計算面積
        perimeter = cv2.arcLength(c, True)  # 計算周長
        squre_L = perimeter/4
        rate = pow(squre_L,2) - area
        epsilon = 0.01 * cv2.arcLength(c, True)
        approx =len( cv2.approxPolyDP(c, epsilon, True))
        abyp = area/perimeter
        #print(approx)
        #所有條件計算完成
        #底下的if才能用

        if abyp<22 and abyp > 3 :#  and approx <15 and approx >5  :
            cv2.putText(image1, "%d"%area, (cX-20,cY), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (252, 197, 5), 3 ,cv2.LINE_AA)
            cv2.putText(image1, "%d" % abyp, (cX+70, cY), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (152, 197, 105), 3,cv2.LINE_AA)
            cv2.putText(image1, "%d"%approx, (cX + 70, cY+50), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (2, 7, 5), 3,cv2.LINE_AA)
            cv2.circle(image1, (cX, cY), 10, (1, 227, 254), -1)

            #cv2.circle(image1, (480, cY), 10, (1, 227, 254), -1)
            #print(j,abyp)
            #print("rate = ", rate)
            print(cX,cY)
        i+=1

    j+=1
    # 在中心點畫上黃色實心圓
    # 在該Contours印上其編號。



cv2.imshow('1',image1)

cv2.waitKey()