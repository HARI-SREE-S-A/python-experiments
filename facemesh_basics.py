import cv2
import mediapipe as mp
import time



mpfacemesh = mp.solutions.face_mesh
facemesh = mpfacemesh.FaceMesh()
mpdraw = mp.solutions.drawing_utils
measurements = mpdraw.DrawingSpec(thickness=1,circle_radius=1)


cap = cv2.VideoCapture(0)
ctime = 0
ptime = 0

while True:

    success , img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results  = facemesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpdraw.draw_landmarks(img,faceLms,mpfacemesh.FACEMESH_CONTOURS,measurements,measurements)
            for id,lm in enumerate (faceLms.landmark):
                h,w,c = img.shape
                cx , cy = int(lm.x*w) , int(lm.y*h)

                print(id,cx,cy)






    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, str(int(fps)), (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    cv2.imshow("harvis",img)
    cv2.waitKey(1)
