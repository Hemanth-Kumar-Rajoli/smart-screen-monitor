import cv2 as cv
import mediapipe as mp
from matplotlib import pyplot as plt
import numpy as np
import math

class HandDetection:
    def __init__(self):
        self.mp_drawingUtils = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.video_status = True
        self.cap = cv.VideoCapture(0)

    def forward(self):
        pass
    def backward(self):
        pass
    def pause(self):
        pass
    def play(self):
        pass
    def volumeUp(self):
        pass
    def volumeDown(self):
        pass
    def checkForPause(self,angles,result): #return true if need to pause any video else play
        pointsOfThumb = self.getRequiredPoints([4,2,0],result)
        a = self.angleBetweenThreePoints(pointsOfThumb[0],pointsOfThumb[1],pointsOfThumb[2])

        return (all([True if angle <=50 else False for angle in angles[1:]]) and a<160)

    def checkForVolume(self,angles): # returns true if firstTwo fingers are opened and last three fingers are closed
        lastThreeClosed = all([True if angle <=70 else False for angle in angles[2:]])
        firstTwoOpened = all([True if angle >=50 else False for angle in angles[:2]])

        return lastThreeClosed and firstTwoOpened

    def videoSkipControl(self,angles,result):
        pointsOfThumb = self.getRequiredPoints([4,2,0],result)
        a = self.angleBetweenThreePoints(pointsOfThumb[0],pointsOfThumb[1],pointsOfThumb[2])

        return (all([True if angle <=50 else False for angle in angles[1:]]) and a>=160)

    def distanceBetweenTwoPoints(self,point1,point2):
        return math.sqrt(math.pow(point1[0]-point2[0],2)+math.pow(point1[1]-point2[1],2))

    def whichHand(self,result):
        if result.multi_handedness[0].classification[0].label.upper()=="LEFT":
            return "LEFT"
        else:
            return "RIGHT"

    def angleBetweenThreePoints(self,point1,point2,point3):
        a=self.distanceBetweenTwoPoints(point1,point2)
        b=self.distanceBetweenTwoPoints(point2,point3)
        c=self.distanceBetweenTwoPoints(point3,point1)
    
        cal = ((a*a+b*b-c*c)/(2*a*b))
        try:
            return math.degrees(math.acos(cal))
        except:
            return 90.0

    def getRequiredPoints(self,joints,result):
        return [(int(result.multi_hand_landmarks[0].landmark[joint].x*640),int(result.multi_hand_landmarks[0].landmark[joint].y*480)) for joint in joints]
    def findAnglesForEveryFinger(self,result):
        finger1 = self.getRequiredPoints([2,3,4],result)
        finger2 = self.getRequiredPoints([5,6,8],result)
        finger3 = self.getRequiredPoints([9,10,12],result)
        finger4 = self.getRequiredPoints([13,14,16],result)
        finger5 = self.getRequiredPoints([17,18,20],result)
        fAngle1 = self.angleBetweenThreePoints(finger1[0],finger1[1],finger1[2])
        fAngle2 = self.angleBetweenThreePoints(finger2[0],finger2[1],finger2[2])
        fAngle3 = self.angleBetweenThreePoints(finger3[0],finger3[1],finger3[2])
        fAngle4 = self.angleBetweenThreePoints(finger4[0],finger4[1],finger4[2])
        fAngle5 = self.angleBetweenThreePoints(finger5[0],finger5[1],finger5[2])
        return [fAngle1,fAngle2,fAngle3,fAngle4,fAngle5]
    def RecognizeHand(self,frame):
        with self.mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5,max_num_hands=1) as hands:
            image_rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    
            results = hands.process(image_rgb)
    
            # image_bgr = cv.cvtColor(image_rgb,cv.COLOR_RGB2BGR)
    
            if results.multi_hand_landmarks:
                for hand in results.multi_hand_landmarks:
                    self.mp_drawingUtils.draw_landmarks(frame,hand,self.mp_hands.HAND_CONNECTIONS,self.mp_drawingUtils.DrawingSpec(color=(121,22,76),thickness=2,circle_radius=4),self.mp_drawingUtils.DrawingSpec(color=(250,44,250),thickness=2,circle_radius=4))
                return results
    def captureHand(self):
        video_status = "play"
        last_distance = 9999
        curr_volume = 100
        while True:
            _,frame = self.cap.read()
            frame = cv.flip(frame,1)
            result = self.RecognizeHand(frame)
            if result is not None:
                angles = self.findAnglesForEveryFinger(result)
                if(self.checkForPause(angles,result)):
                    video_status = "pause"
                    
                if(self.checkForVolume(angles)):
                    points = self.getRequiredPoints([4,8],result)
                    distance = self.distanceBetweenTwoPoints(points[0],points[1])
                    if(distance>last_distance):
                        curr_volume+=1
                    elif(distance<last_distance):
                        curr_volume-=1
                    last_distance=distance
                    cv.putText(frame,"volume control",(300,100),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
                if(self.videoSkipControl(angles,result)):
                    if(self.whichHand(result)=='LEFT'):
                        cv.putText(frame,"forwarding...",(0,100),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
                    else:
                        cv.putText(frame,"backward...",(0,100),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
            cv.putText(frame,video_status,(300,100),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
            cv.putText(frame,f'volume : {curr_volume}',(400,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,0),1)
            video_status="play"
            cv.imshow("frame",frame)
            
            if cv.waitKey(10) & 255 == ord('q'):
                break
        self.cap.release()
        cv.destroyAllWindows()
if __name__ == '__main__':
    HandDetection().captureHand()