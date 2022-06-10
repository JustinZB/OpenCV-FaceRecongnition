import cv2 as cv
img = cv.imread("03.jpg")
cv.imshow("input_image",img)
#修改图片的尺寸
resize_img = cv.resize(img,dsize=(110,160))
print(resize_img.shape)
cv.imshow("resize_img",resize_img)
#如果键盘输入的是1就退出
while True:
    if ord("1")==cv.waitKey(0):
        break
cv.destroyAllWindows()