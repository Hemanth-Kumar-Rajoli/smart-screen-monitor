import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
class DetectFace:
    face_rect = None
    def __init__(self, frame) -> None:
        '''using frontal alt tree to recognize face because it is more sharp in finding faces when compared with others'''
        harr_cascade = cv.CascadeClassifier('public/Recognitions/HaarCascadeFiles/haarcascade_frontalface_default.xml')
        gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        self.face_rect = harr_cascade.detectMultiScale(gray_frame,scaleFactor=1.1,minNeighbors=4)
    '''it will draw rectangle around the faces'''
    def drawFaces(self):
        for (x,y,w,h) in self.face_rect:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    def isThereFace(self):
        return (True if len(self.face_rect)>0 else False)
    def countFaces(self):
        return len(self.face_rect)
    def areaFaces(self):
        return [face[2]*face[3] for face in self.face_rect]
if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    while True:
        isTrue,frame = cap.read()
        
        FacesDetected = DetectFace(frame)
        FacesDetected.drawFaces()
        cv.imshow("face",frame)
        if cv.waitKey(10) & 255 == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
    print("form main")