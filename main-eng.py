from tkinter import *
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse





root = Tk()
r = sr.Recognizer()
engine = pyttsx3.init()
Chrome = webdriver.Chrome(ChromeDriverManager().install())

root.title("Hej Michał")
root.geometry("800x800")

e = Entry(root, width=200)
e.pack(padx = 50)


def Recognize():

    try:
        with sr.Microphone() as source:
            voice = r.listen(source)
            command = r.recognize_google(voice)
            command.lower()
            e.insert(0, command)
            engine.say(command)
            engine.runAndWait()
            if 'play' in command:
                song = command
                song = command.replace("play", "")
                e.delete(0, END)
                e.insert(0, f"Play  {song}")
                engine.say(f"Playing {song} now")
                engine.runAndWait()
                pywhatkit.playonyt(command)
            if 'date' in command:
                CurrentDate = command
                CurrentDate = datetime.datetime.now().replace(microsecond=0, second=0)
                e.delete(0, END)
                e.insert(0, f"Current date: {CurrentDate}")
                engine.say(f"Current date is {CurrentDate}")
                engine.runAndWait()
            if 'weather' in command:
                Weather = command.replace("what's the weather like in","")
                e.delete(0, END)
                e.insert(0, f"Current weather in {Weather}")
                engine.say("Opening Chrome")
                engine.runAndWait()
                Url = f"https://www.weather-forecast.com/locations/{Weather}/forecasts/latest"
                cos = urllib.parse.unquote(Url)
                cos1 = urllib.parse.unquote(Url).replace(" ","") #Usuwa %20 z linku
                Chrome.get(cos1)
            if 'timer' in command:
                def czas(t):
                    while t:
                        mins, secs = divmod(t, 60) 
                        timer = '{:02d}:{:02d}'.format(mins, secs)
                        print(timer, end="\r")
                        time.sleep(1)
                        t -= 1
                        czas(int(t))
                        
                    timer = command.replace('timer set', '')
                    TimerScreen = Toplevel(root)
                    TimerScreen.geometry("400x400")
                    TimerScreen.title("Timer")
                    Label(TimerScreen, text = t).pack()                        
                    e.delete(0, END)
                    e.insert(0, f"Setting timer to: {timer}")
                    engine.say(f"Setting timer to {timer}")
                    engine.runAndWait()
                    if t == 0:
                        engine.say("Time is over!")
                        engine.runAndWait()
                        TimerScreen.destroy()
            

    except:
        e.delete(0,END)
        e.insert(0, "Try again!")
        engine.say("I don't understand you")
        engine.runAndWait()




Przycisk = Button(root, text = "Execute the command!", command=Recognize, width=20, height = 5)
Przycisk.pack(pady = 100)







mainloop()
