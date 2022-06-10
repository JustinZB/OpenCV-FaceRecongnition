import cv2 as cv
src = cv.imread("03.jpg")
cv.imshow("input image",src)
#cv2 读取图片的通道是BGR(蓝绿红)
#PIL读取图片的通道是RGB
gray_img = cv.cvtColor(src,code=cv.COLOR_BGR2GRAY)
cv.imshow("gray_image",gray_img)
cv.waitKey(0)
cv.destroyAllWindows()
#保存图片
cv.imwrite("gray_03.jpg",gray_img)