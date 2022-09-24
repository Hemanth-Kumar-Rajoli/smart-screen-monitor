import subprocess
import pyautogui
import time
import os
class Controlmedia:
    vlcp = "C:/Program Files/VideoLAN/VLC/vlc.exe"
    def __init__(self,videoloc):
        self.videoloc = videoloc
    def Checkvlc(self):
        if (os.path.exists(self.vlcp)):
            print("vlc mediaplayer exist")
        else:
            print("vlc mediaplayer does not exist")
    def Checkvideo(self):
        lst=self.videoloc
        lst=lst.split("\\")
        name=lst[len(lst)-1]
        if (os.path.exists(self.videoloc)):
            print("video exist and name is ",name)
        else:
            print("video does not exist or path is invalid for ",name)
    def openvideo(self):
        p = subprocess.Popen([self.vlcp, self.videoloc])
    @staticmethod
    def volup():
        pyautogui.press("volumeup")
    @staticmethod
    def voldown():
        pyautogui.press("volumedown")
    @staticmethod
    def backward():
        pyautogui.press("left")
    @staticmethod
    def forward():
        pyautogui.press("right")
    @staticmethod
    def pause():
        pyautogui.press(" ")
    @staticmethod
    def play():
        pyautogui.press(" ") 
if __name__ == "__main__":
    p1 = Controlmedia("D:\\movies\\marvel\\MARVEL\\2.captain marvel.mkv")
    p1.Checkvlc()
    time.sleep(3)
    p1.Checkvideo()
    time.sleep(3)
    p1.openvideo()
    time.sleep(3)
    p1.volup()
    time.sleep(3)
    p1.voldown()
    time.sleep(3)
    p1.backward()
    time.sleep(3)
    p1.forward()
    time.sleep(3)
    p1.pause()
    time.sleep(3)
    p1.play()

