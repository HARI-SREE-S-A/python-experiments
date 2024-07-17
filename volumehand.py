import cv2
import mediapipe as mp
import time
import numpy as np
import hndmodule as hmt
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
############################################################
wCam, hCam = 640,480

###########################################################



cTime = 0
pTime = 0
detector = hmt.handDetector()

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volu = volume.GetVolumeRange()

maxvol = volu[1]
minvol = volu[0]



while True:
    success,img = cap.read()
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime


    
    img = detector.findHands(img)
    lmList = detector.findposition(img)
    if len(lmList) !=0:
        #print(lmList[4],[8])
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]
        cx,cy = (x1+x2)//2,(y1+y2)//2

        cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1)
       # print(length)
        vol = np.interp(length,[25,200],[minvol,maxvol])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)
        if length <50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)


    cv2.putText(img,str(int(fps)),(10,80),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


    cv2.imshow("image",img)

    cv2.waitKey(1)
