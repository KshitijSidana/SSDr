import cv2
from movement import minimiseError
from multiprocessing.pool import ThreadPool
#from movement import stopMovement
# cascade code
def readVideo(cap):
    return cap.read()

def face_cascade1(img, num1=1.2, num2=3):
         return face_cascade.detectMultiScale(img, num1, num2)

def minimun(x,y,z,w):
     minimiseError(x,y,z,w) 

face_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
cap = cv2.VideoCapture(0)

pool =ThreadPool(processes=1)
pool2=ThreadPool(processes=2)
pool3=ThreadPool(processes=3)

while 1:
    result=pool.apply_async(readVideo,(cap,))
    ret, img = result.get()
    img=cv2.pyrDown(img) #improved detection and speed
    #img=cv2.pyrDown(img)
    result2=pool2.apply_async(face_cascade1,(img,))
    faces = result2.get() # for 1.1, 5 for full body
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        #print(y, y + h)
        #print(x, x + w)
        pool3.apply_async(minimun,(x,y,x+w,y+h))
    cv2.rectangle(img, (100, 70), (230, 220), (255, 0, 0), 2)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
#stopMovement();



