import cv2
import mediapipe as mp

####################################################################

class posedetector():
    def __init__(self,mode=False,model_complexity=1,upbody=False,smooth=True,detcon=0.5,trackon=0.5):
        self.mode = mode
        self.model_complexity=model_complexity
        self.upbody = upbody
        self.smooth = smooth
        self.detcon = detcon
        self.trackon = trackon

        self.mppose = mp.solutions.pose
        self.pose = self.mppose.Pose(self.mode,self.model_complexity,self.upbody,self.smooth,self.detcon,self.trackon)
        self.mpdraw = mp.solutions.drawing_utils



    def findpose(self,img) :
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            self.mpdraw.draw_landmarks(img, self.results.pose_landmarks, self.mppose.POSE_CONNECTIONS)


        return img





    def getposition(self,img):
        lmList=[]
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)
                lmList.append([id,cx,cy])
        return lmList











def main():
    cap = cv2.VideoCapture(0)
    det = posedetector()
    while True:
        success, img = cap.read()
        img = det.findpose(img)
        lmList = det.getposition(img)
        print(lmList)











        cv2.imshow("harvsi", img)
        cv2.waitKey(1)









if __name__ == "__main__":
    main()