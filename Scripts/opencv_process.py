import numpy as np
import cv2

import matplotlib.pyplot as plt
image = cv2.imread('C:\\Users\\user\\Desktop\\AI_dataset\\car_view\\S4.jpg')
image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_CUBIC)
kernel_size = 3
image_blur = cv2.GaussianBlur(image,(kernel_size, kernel_size), 0)
hsv_img = cv2.cvtColor(image_blur,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv_img)
#paper_low=np.array([26,43,46])
#paper_high=np.array([34,255,255])

paper_low_2 = np.array([11, 43, 46])
paper_high_2 = np.array([25, 255, 255])
#lower_green = np.array([35, 43, 46])
#upper_green = np.array([77, 255, 255])
curr_mask =  cv2.inRange(hsv_img,paper_low_2,paper_high_2)
#curr_mask2=cv2.inRange(hsv_img,paper_low,paper_high)
#curr_mask3=cv2.inRange(hsv_img,lower_green,upper_green )
#bitwiseOr = cv2.bitwise_or(curr_mask2,curr_mask3)
#cv2.imshow('bitwiseOr = ',bitwiseOr)
mask = curr_mask#+curr_mask2+curr_mask3
cv2.imshow('mask = ',mask)
hsv_img[mask >0 ] = ([140,70,30])
cv2.imshow('cur_mask',hsv_img)

cv_rgb = cv2.cvtColor(image_blur,cv2.COLOR_BGR2RGB)
#plt.imshow(cv_rgb)
#plt.show()
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)

gray = cv2.cvtColor(masked, cv2.COLOR_RGB2GRAY) #grayscale conversion
low_threshold = 10
high_threshold = low_threshold*3
kernel_size = 13
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
cv2.imshow('canny',edges)
contours, hierarch = cv2.findContours(mask, cv2.RETR_CCOMP, 2)
print(len(contours))
area_list= []
for c in contours:
    area = cv2.contourArea(c)
    area_list.append(area)
for c in contours:
    # CV2.moments會傳回一系列的moments值，我們只要知道中點X, Y的取得方式是如下進行即可。
    area = cv2.contourArea(c)

    if (area>max(area_list)-500 and area > 500 ):
        M = cv2.moments(c)
        if(M["m00"]!= 0):
            cX = int(M["m10"] / M["m00"])

            cY = int(M["m01"] / M["m00"])
        # 在中心點畫上黃色實心圓
            cv2.circle(image, (cX, cY), 10, (1, 227, 254), -1)
        #cv2.drawContours(image,c, -1, (0, 255, 255), 3)
        approx = cv2.approxPolyDP(c, int(max(area_list)/2420), True)
        print(int(max(area_list)/242))
        #cv2.polylines(image, [approx], True, (0, 255, 0), 2)
cv2.imshow('image', image)
print(max(area_list))

#cv_rgb = cv2.cvtColor(hsv_img,cv2.COLOR_BGR2RGB)
#plt.imshow(cv_rgb)
#plt.show()

cv2.waitKey(0)

