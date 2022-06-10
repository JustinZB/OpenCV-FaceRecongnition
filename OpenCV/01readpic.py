#导入需要的模块
import cv2 as cv
#读取图片
img = cv.imread("03.jpg")
#显示图片
cv.imshow("read_img",img)
#等待键盘输入 单位毫秒 0表示无线等待
cv.waitKey(0)
#释放内存
cv.destroyAllWindows()

