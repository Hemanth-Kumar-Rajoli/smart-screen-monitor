import subprocess
import pyautogui
import time
import os
class Controlmedia:
    vlcp = "C:/Program Files (x86)/VideoLAN/VLC/vlc.exe"
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
    def volup(self):
        pyautogui.press("volumeup")
    def voldown(self):
        pyautogui.press("volumedown")
    def backward(self):
        pyautogui.press("left")
    def forward(self):
        pyautogui.press("right")
    def pause(self):
        pyautogui.press(" ")
    def play(self):
        pyautogui.press(" ")
p1 = Controlmedia("C:\\Users\\AKRAM\\Downloads\\Vikram-Telugu-s5rtu-2022.mp4")
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

