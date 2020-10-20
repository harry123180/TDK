import matplotlib.pyplot as plt
#這個是查看圖片座標的程式
#img_matplot=plt.imread("C:\\Users\\user\\Desktop\\TDK_program\\Scripts\\view_data\\output1.jpg")
img_matplot =plt.imread('C:\\Users\\user\\Desktop\\TDK_program\\Scripts\\view_data\\pic1.jpg')
#img_matplot = plt.imread('D:\\TDKsPicture\\CX0\\100cm1.jpg')
#img_matplot = plt.imread('D:\\TDKsPicture\\targetline\\view3.jpg')
plt.figure("matplotWin")
plt.imshow(img_matplot)
plt.show()