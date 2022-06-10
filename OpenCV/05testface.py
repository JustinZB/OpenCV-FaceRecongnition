import cv2 as cv
def face_detect_demo():
    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    #加载特征数据
    face_detector = cv.CascadeClassifier("D:/pythonprojects/OpenCV-FaceRecongnition/OpenCV/cascade/haarcascade_frontalface_default.xml")
    faces = face_detector.detectMultiScale(gray,1.02,5)
    for x,y,w,h in faces:
        cv.rectangle(src,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
    cv.imshow('result',src)
src = cv.imread('03.jpg')
face_detect_demo()
cv.waitKey(0)
cv.destroyAllWindows()