import cv2
from movement import minimiseError
#from thread import start_new_thread as snT
#from movement import stopMovement

# cascade code

face_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    img=cv2.pyrDown(img) #improved detection and speed
    #img=cv2.pyrDown(img)
    faces = face_cascade.detectMultiScale(img, 1.2, 3)  # for 1.1, 5 for full body
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        #print(y, y + h)
        #print(x, x + w)
        minimiseError(x,y,x+w,y+h)    #call for movement
    cv2.rectangle(img, (100, 70), (230, 220), (255, 0, 0), 2)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
#stopMovement();



