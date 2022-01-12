from cv2 import cv2
import cvzone
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
overlay=cv2.imread('star.png',cv2.IMREAD_UNCHANGED)
while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in face:
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        overlay_resize = cv2.resize(overlay, (int(w), int(h)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x +5, y - 13])
        original_frame = frame.copy()
        face_roi = frame[y:y + h, x:x + w]
        gray_roi = gray[y:y + h, x:x + w]
        smile = smile_cascade.detectMultiScale(gray_roi, 1.7, 25)
        for (x1, y1, w1, h1) in smile:
            cv2.rectangle(face_roi, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)
            cv2.imwrite('PICTURE.png', original_frame)
    cv2.imshow('SNAPCHAT', frame)
    if cv2.waitKey(10) == ord('q'):
        break