import cv2
import time
import os
import hand_tracking_module as htm
wCam, hCam = 1288, 728
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handdetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    img = detector.findhands(img)
    lmList = detector.findposition(img, draw=False)
    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)
        cv2.putText(img, str(totalFingers), (30, 400), cv2.FONT_HERSHEY_PLAIN,10, (255, 0, 0), 5)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.imshow("Image", img)
    if cv2.waitKey(5) & 0xFF==ord('K'):
        break
            
    