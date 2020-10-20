import cv2
import numpy as np
image1=cv2.imread('C:\\Users\\user\\Pictures\\ph\\s1.jpg')

gaus = image1#cv2.GaussianBlur(image1, (3, 3), 0)
hsv_img = cv2.cvtColor(gaus, cv2.COLOR_BGR2HSV)
edges = cv2.Canny(gaus, 50, 150, apertureSize=3)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
dilated = cv2.dilate(edges, kernel)
losed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("di",dilated)
image_masked = cv2.add(gaus, np.zeros(np.shape(gaus), dtype=np.uint8), mask=losed)
cv2.imshow('masked',image_masked)
cv2.imshow('gaus',gaus)
cv2.imshow('edges',edges)
cv2.imshow('window',losed)
cv2.imwrite('output.jpg', image_masked)

cv2.waitKey()