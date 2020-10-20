import cv2
import numpy as np
import math
from PIL import Image

#image1 = cv2.imread('D:\\TDKsPicture\\targetline\\view3.jpg') #這個是隨身碟的
image1 = cv2.imread('C:\\Users\\user\\Desktop\\TDK_program\\Scripts\\view_data\\s2.jpg')
image1 = cv2.resize(image1, (640, 480), interpolation=cv2.INTER_CUBIC)
# y = 46 +- 10
# x = 120 to 355
# y=157
# x=258 577
x_range = [270, 337]
y_range = [202, 228]


def mask_area(image, distance):
    y_pixel = int(52.11 * math.log(distance) - 124.07)
    size = image.shape
    x_max = size[1]
    sss = np.zeros([480, 640], dtype=np.uint8)
    sss[y_range[0]:y_range[1], x_range[0]:x_range[1]] = 255
    cv2.imshow('sss',sss)

    kernel_size = 3

    gaus = cv2.GaussianBlur(image1, (7, 7), 0)
    hsv_img = cv2.cvtColor(gaus, cv2.COLOR_BGR2HSV)
    black_low = np.array([0, 0, 0])
    black_high = np.array([180, 255, 46])
    b_low = np.array([0, 0, 46])
    b_high = np.array([180, 43, 76])
    # 顏色過濾
    ranged = cv2.inRange(hsv_img, black_low, black_high)
    ranged2 = cv2.inRange(hsv_img, b_low, b_high)
    ranged = ranged + ranged2
    #cv2.imshow('ranged', ranged)
    # gray = cv2.cvtColor(ranged, cv2.COLOR_BGR2GRAY)
    # 定义结构元素
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    edges = cv2.Canny(ranged, 50, 150, apertureSize=3)

    # 膨胀图像
    # dilated = cv2.dilate(edges, kernel)
    # cv2.imshow("di",dilated)
    # 闭运算
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    #cv2.imshow("closed", closed)

    # image_blur = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    # hsv_img = cv2.cvtColor(image_blur, cv2.COLOR_BGR2HSV)

    minLineLength = 10
    maxLineGap = 2

    pit = ranged

    # mask = curr_mask
    image_masked = cv2.add(pit, np.zeros(np.shape(pit), dtype=np.uint8), mask=sss)
    lines = cv2.HoughLinesP(image_masked, 1, np.pi / 180, 100, minLineLength=minLineLength, maxLineGap=maxLineGap)
    (cnts, _) = cv2.findContours(pit, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        # CV2.moments會傳回一系列的moments值，我們只要知道中點X, Y的取得方式是如下進行即可。

        M = cv2.moments(c)
        if(M["m00"]!=0):
            cX = int(M["m10"] / M["m00"])

            cY = int(M["m01"] / M["m00"])



        # 在中心點畫上黃色實心圓

        cv2.circle(pit, (cX, cY), 10, (1, 227, 254), -1)
    #print("現有幾條", len(lines))
    #for t in range(len(lines)):
        #for x1, y1, x2, y2 in lines[t]:
            #cv2.line(image1, (x1, y1), (x2, y2), (0, 255, 0), 6)
    #cv2.imshow("123",sss)
    #cv2.imshow("masked", image_masked)
    #cv2.imshow("edges", pit)

    image = Image.fromarray(cv2.cvtColor(image_masked, cv2.COLOR_BGR2RGB))
    #image.show()
    return image_masked


image1 = mask_area(image1, 400)
cv2.imshow('window', image1)
cv2.waitKey()