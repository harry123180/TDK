import numpy as np #1
import cv2 #2
#這個是查看圖片座標的程式
canvas=cv2.imread("C:\\Users\\user\\Desktop\\TDK_program\\Scripts\\view_data\\output1.jpg")
green = (0, 255, 0) #4
cv2.line(canvas, (209, 474), (271, 301), green,5) #5
cv2.imshow("Canvas", canvas) #6
cv2.waitKey(0) #7