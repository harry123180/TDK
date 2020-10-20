import cv2
import math
import numpy as np




#image1 = cv2.imread('C:\\Users\\user\\Desktop\\TDK_program\\Scripts\\view_data\\s2.jpg') #讀圖


x_range = [0,640]
y_range = [0 , 480]

#y_pixel = int(52.11 * math.log(distance) - 124.07)
#size = image.shape # 取圖片座標
#x_max = size[1]
sss = np.zeros([480, 640], dtype=np.uint8)
#sss[圖片最上面y:圖片最下方y, 圖片最左邊x:圖片最右邊x] = 255 這個抓ROI

# pic = cv2.resize(pic, (400, 400), interpolation=cv2.INTER_CUBIC) 圖片 大小 更改圖片尺寸

#   gaus = cv2.GaussianBlur(image1, (7, 7), 0)#  高斯模糊

# hsv_img = cv2.cvtColor(gaus, cv2.COLOR_BGR2HSV)  #轉hsv
#    black_low = np.array([0, 0, 0]) #hsv下限設定
#    black_high = np.array([180, 255, 46]) #hsv上限設定
#ranged = cv2.inRange(hsv_img, black_low, black_high) #hsv 顏色過濾

# 膨胀图像
# dilated = cv2.dilate(edges, kernel)

# 闭运算
#   closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

#把ROI罩上去
#image_masked = cv2.add(pit, np.zeros(np.shape(pit), dtype=np.uint8), mask=sss)

#霍夫找線
# minLineLength = 10
# maxLineGap = 2
#lines = cv2.HoughLinesP(image_masked, 1, np.pi / 180, 100, minLineLength=minLineLength, maxLineGap=maxLineGap)
#邊緣算法
#edges = cv2.Canny(ranged, 50, 150, apertureSize=3)
#找中點
"""
(cnts, _) = cv2.findContours(pit, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        # CV2.moments會傳回一系列的moments值，我們只要知道中點X, Y的取得方式是如下進行即可。

        M = cv2.moments(c)
        if(M["m00"]!=0):
            cX = int(M["m10"] / M["m00"])

            cY = int(M["m01"] / M["m00"])

"""
# for t in range(len(lines)):
# for x1, y1, x2, y2 in lines[t]:
# cv2.line(image1, (x1, y1), (x2, y2), (0, 255, 0), 6)

