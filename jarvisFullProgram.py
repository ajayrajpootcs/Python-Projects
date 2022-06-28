import pyttsx3
import time
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess
import os
import multiprocessing
from playsound import playsound
import random
import sys
import pyautogui
import wmi
from pytube import YouTube
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Jarvish import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def wishme(self):
    playsound('E:\\Ajay Rajpoot\\MY CODES\\JARVISH\\jarv.mp3')
    hour = int(datetime.datetime.now().hour)
    tm = time.strftime("%I:%M:%p")
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon, its {tm}")
    else:
        speak(f"Good Evening, its {tm}")
    speak(" TEAM AR Please tell me What can i do for you")

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TaskExicution()
    def takecommond(self):
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)      
        try:
            print("Recongnizing...")
            query= r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Please say that again ..")
            return "None"
        return query
    def TaskExicution(self):
        wishme(self)
        while True:
            self.query = self.takecommond().lower()
            if 'wikipedia' in self.query:
                speak('searching Wikipedia...')
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query,sentences=2)
                speak("According to Wikipedia..")
                print(results)
                speak(results)
            elif 'open youtube' in self.query:
                speak("ok sir   opening youtube")
                webbrowser.open("youtube.com")
            elif "play song on youtube" in self.query:
                speak("which song do you want to play")
                song = self.takecommond()
                speak(" do you want to listen single song ")
                speak("And after listening close the song")
                speak("for single please say, Yes or for multipule songs say, No")
                ff = self.takecommond()
                web = "https://www.youtube.com/results?search_query={}".format(song)
                webbrowser.open_new_tab(web)
                time.sleep(12)
                pyautogui.click(650, 320)
                if "yes" in ff:
                    time.sleep(200)
                    pyautogui.hotkey("Alt","f4")
                elif "no" in ff:
                    speak("ok sir")
            elif 'play music' in self.query or "play song" in self.query:
                music_dir = 'E:\\Ajay Rajpoot\\RMX1827_11_C.16\\English Music'
                songs = os.listdir(music_dir)
                print(songs)
                n = random.randint(0,86)
                speak("playing song")
                os.startfile(os.path.join(music_dir,songs[n]))
            elif 'love you' in self.query:
                engine.setProperty('voice',voices[1].id)
                speak('love you two')
            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir , the time is {strTime}")
            elif ('open code' or 'code') in self.query:
                speak("opening code")
                subprocess.Popen('C:\\Users\\apna\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe')
            elif 'notepad' in self.query:
                speak("opening notepad")
                subprocess.Popen('C:\\Windows\\system32\\notepad.exe')
            elif 'turbo' in self.query:
                speak('opening turbo c')
                subprocess.Popen('C:\\TURBOC3\\Turbo C++\\Turbo C++.exe')
            elif 'whatsapp' in self.query:
                subprocess.Popen('C:\\Users\\apna\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
            elif 'browser' in self.query:
                subprocess.Popen('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
            elif 'goodbye' in self.query:
                speak("thanks for using me, sir ,you can call me any time ")
                sys.exit()
            elif ('shutdown' or 'power off') in self.query:
                speak("system going to shutdown")
                os.system("shutdown /s /t 1")
            elif 'restart' in self.query:
                os.system("shutdown /r /t 1")
            elif "download video" in self.query:
                speak('please enter your link')
                youtube_video_url = input('enter link like https://www.youtube.com/watch?v=W-XLz9AeGLk\n')
                try:
                    yt_obj = YouTube(youtube_video_url)
                    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
                    # download the highest quality video
                    filters.get_highest_resolution().download()
                    speak('Video Downloaded Successfully')
                except Exception as e:
                    print(e)
            elif  'google search' in self.query: 
                speak('what do you want to search on google, sir')
                search_terms = self.takecommond()
                speak(f"searching {search_terms}")
                url = "https://www.google.com.tr/search?q={}".format(search_terms)
                chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
                chrome_browser.open_new_tab(url)
            elif "find from my pc" in self.query or "search from my pc" in self.query:
                speak('what do you want to find, sir')
                i = 0
                inp = self.takecommond()
                thisdir = os.getcwd()
                for r, d, f in os.walk("E:\\"): # change the hard drive, if you want
                    for file in f:
                        filepath = os.path.join(r, file)
                        if inp in file:
                            os.startfile(filepath)
                            print(filepath)
                            i = i+1
                if i == 0:
                    speak("sorry sir, no files found please try again")
                else:
                    speak("opening searched files")
                print(f"trovati {i} files.") 
            elif "close" in self.query:
                pyautogui.hotkey("Alt","f4")
            elif 'hide' in self.query:
                pyautogui.hotkey("win",'d')
            elif "running process" in self.query:
                f = wmi.WMI()
                print("pid   Process name")
                for process in f.Win32_Process():
                    print(f"{process.ProcessId:<10} {process.Name}")
            elif "open command prompt" in self.query:
                speak("opening command prompt")
                os.system("start cmd")
startExicution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/apna/Downloads/GRAPHICS DESIGNING/wallpaper2you_347368.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/apna/Downloads/GRAPHICS DESIGNING/smile_loader_by_gleb.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/apna/Downloads/GRAPHICS DESIGNING/e8c5b61a18d49c20c48f0fe6d4839def4a96d970r1-444-250_hq.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/apna/Downloads/GRAPHICS DESIGNING/team.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/apna/Downloads/GRAPHICS DESIGNING/me.jpg")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/apna/Downloads/GRAPHICS DESIGNING/Private GIF.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/apna/Downloads/GRAPHICS DESIGNING/See every Iron Man suit from the Marvel movies in a single GIF.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExicution.start()
    def showTime(self):
        ct = QTime.currentTime()
        cd = QDate.currentDate()
        label_time = ct.toString('hh:mm:ss')
        lavel_date = cd.toString(Qt.ISODate)
        self.ui.textBrowser.setText(lavel_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
Jarvish = Main()
Jarvish.show()
exit(app.exec())

if __name__ == "__main__":
    TaskExicution(self)