import cv2 as cv
import numpy as np
import time
import math
# 選擇第二隻攝影機
cap = cv.VideoCapture(0)
#size = cap.shape
#print(size)
while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()
  size = frame.shape
  # 顯示圖片
  start = time.time()
  whitle_low = np.array([100, 43, 46])
  whitle_high = np.array([124, 255, 255])
  hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
  curr_mask = cv.inRange(hsv_img, whitle_low, whitle_high)
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  blured = cv.blur(gray, (7, 7))
  kernel = np.ones((5, 5), np.uint8)
  dilation = cv.dilate(blured, kernel, iterations=1)
  #cv.imshow('di', dilation)
  low_threshold = 10
  high_threshold = 110
  edges = cv.Canny(dilation, low_threshold, high_threshold)

  cnts, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
  lines = cv.HoughLinesP(edges, 1, math.pi / 180, 100, 1, 1)
  # lines = cv.HoughLines(edges, 1, math.pi/180, 5)

  line_image = np.copy(frame) * 0
  single = []
  total = []
  if(len(lines)!=0):

      for x in range(len(lines)):  # 列舉出所有的線段
          p1x = lines[x][0][0]
          p1y = lines[x][0][1]
          p2x = lines[x][0][2]
          p2y = lines[x][0][3]
          pt1 = (p1x, p1y)
          pt2 = (p2x, p2y)
          cv.line(frame, pt1, pt2, (30, 75, 25), 3)
      cnt = 0  # 計算線號
      yi = []  # 儲存截距
      stand = []  # 量級
      line_num = []  # 線號存放
      stand_of_lines_number = []  # 量級對應的線號
      all_line_x = []  # 所有線的x點
      for line in lines:
          x1, y1, x2, y2 = line.reshape(4)
          all_line_x.append(x1)
          parameters = np.polyfit((x1, x2), (y1, y2), 1)
          slope = parameters[0]  # 斜率
          y_intercept = parameters[1]  # 截距
          cnt += 1
          if (slope < 0.1 and slope > -0.1):
              line_num.append(cnt)
              yi.append(y_intercept)
      state_of_join_stand = False
      for num in range(len(yi)):  # 做量級分類
          state_of_join_stand = False
          if (num != 0):
              for i in range(len(stand)):
                  if ((yi[num] - stand[i][0]) < 10 and (yi[num] - stand[i][0]) > -10):
                      state_of_join_stand = True
                      stand[i].append(yi[num])
                      stand_of_lines_number[i].append(line_num[num])
          if (state_of_join_stand == False):
              stand.append([yi[num]])
              stand_of_lines_number.append([line_num[num]])
      lines_x = [[] for _ in range(len(stand_of_lines_number))]
      for j1 in range(len(stand_of_lines_number)):
          for j in range(len(stand_of_lines_number[j1])):
              lines_x[j1].append(all_line_x[stand_of_lines_number[j1][j]-1])
      for ouo in range(len(lines_x)):
          cv.line(frame, (max(lines_x[ouo]), int(stand[ouo][0])), (min(lines_x[ouo]), int(stand[ouo][0])), (0, 0, 255), 3)

      end = time.time()
  cv.imshow('frame', frame)

  # 若按下 q 鍵則離開迴圈
  if cv.waitKey(1) & 0xFF == ord('q'):
    break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv.destroyAllWindows()