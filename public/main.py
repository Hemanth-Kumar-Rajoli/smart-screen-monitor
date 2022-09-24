import cv2 as cv
from matplotlib import pyplot as plt
import mediapipe as mp
from mediaController.mediaController import Controlmedia
from Recognitions.handDetection.handDection import HandDetection
from tkinter import filedialog
import time
import threading
if __name__ == '__main__':
    file = filedialog.askopenfile(initialdir="../")
    path = file.name.replace('/','\\') 

    print(path)
    mediaController = Controlmedia(path)
    t1 = threading.Thread(target=mediaController.openvideo)
    t2 = threading.Thread(target=HandDetection().captureHand)
    t2.start()
    time.sleep(1)
    t1.start()
    # mediaController.openvideo()
    # HandDetection().captureHand()

    
    


