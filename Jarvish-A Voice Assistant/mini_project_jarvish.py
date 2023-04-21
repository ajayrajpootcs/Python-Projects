import pyttsx3
import time
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess
import os
import random
import sys
import pyautogui
import wmi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    tm = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon, its{tm}")
    else:
        speak(f"Good Evening, its {tm}")
    speak(" I am Jarvish Upgraded Version")
    speak("by TEAM AR Please tell me What can i do for you")
def takecommond():
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
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommond().lower()
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia..")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("ok sir   opening youtube")
            webbrowser.open("youtube.com")
        elif ("play song on youtube" or "play video") in query:
            speak("which song do you want to play")
            song = takecommond()
            chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            chrome_browser.open_new_tab(song)


            
        elif 'open chrome' in query:
            subprocess.Popen('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
        
        elif 'play music' in query:
            music_dir = 'E:\\Ajay Rajpoot\\RMX1827_11_C.16\\English Music'
            songs = os.listdir(music_dir)
            print(songs)
            n = random.randint(0,86)
            os.startfile(os.path.join(music_dir,songs[n]))
        elif 'i love you' in query:
            engine.setProperty('voice',voices[1].id)
            speak('i love you two')
        elif ('the time' or 'time') in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time is {strTime}")
        elif ('open code' or 'code') in query:
            subprocess.Popen('C:\\Users\\apna\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe')
        elif 'exit' in query:
            sys.exit(0)
        elif 'goodbye'  in query:
            speak("thanks for using me, sir ,you can call me any time ")
            sys.exit(0)
        elif ('search' or 'google search') in query:
            speak('what do you want to search on google, sir')
            search_terms = takecommond()
            url = "https://www.google.com.tr/search?q={}".format(search_terms)
            chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            chrome_browser.open_new_tab(url)
        elif "find something from my pc" in query:
            speak('what do you want to find, sir')
            i = 0
            inp = takecommond()
            thisdir = os.getcwd()
            for r, d, f in os.walk("E:\\"): # change the hard drive, if you want
                for file in f:
                    filepath = os.path.join(r, file)
                    if inp in file:
                        os.startfile(filepath)
                        print(filepath)
                        i = i+1

            print(f"trovati {i} files.") 
        elif "close it" in query:
            pyautogui.hotkey("Alt","f4")
        elif "running process" in query:
            f = wmi.WMI()
            print("pid   Process name")
            for process in f.Win32_Process():
                print(f"{process.ProcessId:<10} {process.Name}")
    
            



                    


            
            

              


            

        	            
                    
               
