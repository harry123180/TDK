import cv2
import numpy as np
import math
def mask_area(image,distance):
    y_pixel = int(52.11*math.log(distance)-124.07)
    size = image.shape
    x_max=size[1]
    sss = np.zeros([480, 640], dtype=np.uint8)
    sss[y_pixel:size[1],0:x_max ] = 255
    #sss[300:350, 310:400] = 255
    print("xmax = ",x_max)
    kernel_size = 3
    image_blur = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    hsv_img = cv2.cvtColor(image_blur, cv2.COLOR_BGR2HSV)
    paper_low = np.array([26, 43, 46])
    paper_high = np.array([34, 255, 255])
    paper_low_2 = np.array([11, 43, 46])
    paper_high_2 = np.array([25, 255, 255])
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    curr_mask = cv2.inRange(hsv_img, paper_low_2, paper_high_2)
    curr_mask2 = cv2.inRange(hsv_img, paper_low, paper_high)
    curr_mask3 = cv2.inRange(hsv_img, lower_green, upper_green)
    #image_masked = cv2.add(mask, np.zeros(np.shape(mask), dtype=np.uint8), mask=sss)
    #bitwiseOr = cv2.bitwise_or(curr_mask2,curr_mask3)
    #cv2.imshow('bitwiseOr = ',bitwiseOr)
    mask = curr_mask + curr_mask2 + curr_mask3
    image_masked = cv2.add(mask, np.zeros(np.shape(mask), dtype=np.uint8), mask=sss)
    cv2.imshow("123",sss)
    return image_masked



image1 = cv2.imread('D:\\TDKsPicture\\output9.jpg')
"""
image2 = cv2.imread('D:\\camera\\ob\\output3.jpg')
image3 = cv2.imread('D:\\camera\\ob\\output4.jpg')
image4 = cv2.imread('D:\\camera\\ob\\output5.jpg')
image5 = cv2.imread('D:\\camera\\ob\\output6.jpg')
image6 = cv2.imread('D:\\camera\\ob\\output7.jpg')
"""
cv2.imshow('org1',image1)
"""
cv2.imshow('org2',image2)
cv2.imshow('org3',image3)
cv2.imshow('org4',image4)
cv2.imshow('org5',image5)
cv2.imshow('org6',image6)
"""
img1 = mask_area(image1,400)
cv2.imshow("mask",img1)
image=cv2.add(image1, np.zeros(np.shape(image1), dtype=np.uint8), mask=img1)
# 找出所有Contours

(cnts, _) = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#clone = img1.copy()

# 依次處理每個Contours
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
        print(approx)
        if abyp<10 and abyp > 4 and rate <100 :
            cv2.putText(image1, "%d"%area, (cX-20,cY), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (252, 197, 5), 3 ,cv2.LINE_AA)
            cv2.putText(image1, "%d" % abyp, (cX+70, cY), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (152, 197, 105), 3,cv2.LINE_AA)
            cv2.putText(image1, "%d"%approx, (cX + 70, cY+50), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (2, 7, 5), 3,cv2.LINE_AA)
            cv2.circle(image1, (cX, cY), 1, (1, 227, 254), -1)
            print(j,abyp)
            print("rate = ", rate)
        i+=1

    j+=1
    # 在中心點畫上黃色實心圓
"""
for cnt_num in range(len(cnts)):
    epsilon = 0.01 * cv2.arcLength(cnts[cnt_num], True)
    approx = cv2.approxPolyDP(cnts[cnt_num], epsilon, True)
    cv2.drawContours(image1, cnts, cnt_num, (225, 255, 0), 2)
    # 分析幾何形狀
    corners = len(approx)
    #print(corners)
"""



    # 在該Contours印上其編號。


"""
img2 = mask_area(image2)
img3 = mask_area(image3)
img4 = mask_area(image4)
img5 = mask_area(image5)
img6 = mask_area(image6)
"""
cv2.imshow('1',image1)
"""
cv2.imshow('2',img2)
cv2.imshow('3',img3)
cv2.imshow('4',img4)
cv2.imshow('5',img5)
cv2.imshow('6',img6)
"""
cv2.waitKey()