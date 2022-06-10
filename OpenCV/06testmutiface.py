import cv2 as cv
def face_detect_demo():
    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    #加载特征数据
    face_detector = cv.CascadeClassifier("D:/pythonprojects/OpenCV-FaceRecongnition/OpenCV/cascade/haarcascade_frontalface_default.xml")
    faces = face_detector.detectMultiScale(gray,1.02,5)
    for x,y,w,h in faces:
        cv.rectangle(src,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
        cv.circle(src,center=(x+w//2,y+h//2),radius=w//2,color=(0,0,255),thickness=2)
    cv.imshow('result',src)
src = cv.imread('04.jpg')
face_detect_demo()
cv.waitKey(0)
cv.destroyAllWindows()