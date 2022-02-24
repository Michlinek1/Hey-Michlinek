from installer import Installing

Installing()
import datetime
import os
import urllib.parse
import webbrowser
from tkinter import *

import pyttsx3
import pywhatkit
import speech_recognition as sr
from translate import Translator
from langdetect import detect, DetectorFactory #Changing it soon (Doesn't work correctly)
from Feelings import *


root = Tk()
r = sr.Recognizer()
engine = pyttsx3.init()

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
                    url = f'https://www.weather-forecast.com/locations/{Weather}/forecasts/latest'
                    urllib.parse.unquote(url)
                    cos1 = urllib.parse.unquote(url).replace(" ","") #Usuwa %20 z linku
                    webbrowser.open(cos1, new=2)
            if 'save' in command:
                f = open("List.txt", "r")
                Saving = command.replace('save', '')
                SavingTxt = [Saving]
                e.delete(0, END)
                e.insert(0  , Saving)
                engine.say(f"Saving {Saving}")
                engine.runAndWait()
                with open('List.txt', "a") as f:
                    f.writelines(SavingTxt)
                    f.close()
            if 'read' in command:
                with open('List.txt', "r") as f:
                    ReadLines = f.readlines()
                    f.close()
                e.delete(0, END)
                e.insert(0, "Reading your saved lines")
                engine.say(f"Saved lines: {ReadLines}")
                engine.runAndWait()
                e.delete(0, END)
                e.insert(0, "Saying...")
                Feelings()
            if 'help' in command:
                Help = Toplevel(root)
                Help.title("Available commands")
                Help.geometry("800x800")
                Label(Help, text = f"Available commands:\nplay\ndate\nweather\nsave\nread\nclose - Depends of file's location\nfeel", font=('Helvetica bold',25)).pack()
            if 'close' in command:
                close = command.replace('close','')
                e.delete(0, END)
                e.insert(0, f"Closing {close}")
                engine.say(f"Closing {close} now")
                engine.runAndWait()
                os.system(f"TASKKILL /F /IM {close}.exe")
            if 'Translate' in command:
                def Translate():
                    DetectorFactory.seed = 0
                    LangDetect = detect(x.get())
                    if str(Stringx.get()) == "1":
                        trans = Translator(to_lang="pl")
                        translation = trans.translate(x.get())
                        Label(TransWindow, text = f"Translated from {LangDetect} to Polish: {translation}").pack()
                    elif str(Stringx.get()) == "2":
                        trans = Translator(to_lang="es")
                        translation = trans.translate(x.get())
                        Label(TransWindow, text = f"Translated from {LangDetect} to Spanish: {translation}").pack()
                    elif str(Stringx.get()) == "3":
                        trans = Translator(to_lang="de")
                        translation = trans.translate(x.get())
                        Label(TransWindow, text = f"Translated from {LangDetect} to German: {translation}").pack()
                    else:
                        Label(TransWindow, text = f"error").pack()
            
            
            if 'password' in command:
                e.delete(0,END)
                e.insert(0,"Opening Password Checker now")
                engine.say("Opening password checker")
                engine.runAndWait()
                os.system("python passchecker.py")



                    
                engine.say("Opening translator now")
                engine.runAndWait()
                TransWindow = Toplevel(root)
                TransWindow.title("Translator")
                TransWindow.geometry("800x800")
                x = Entry(TransWindow, width=200)
                x.pack(padx = 50)
                Stringx = StringVar()
                Radiobutton(TransWindow, text="Polish", variable=Stringx, value = 1 , command = Translate).pack()
                Radiobutton(TransWindow, text="Spanish", variable=Stringx, value = 2 , command = Translate).pack()
                Radiobutton(TransWindow, text="German", variable=Stringx, value = 3 , command = Translate).pack()




            else:
                e.delete(0, END)
                e.insert(0, command)


                 
  
    except:
        e.delete(0,END)
        e.insert(0, "Try again!")
        engine.say("I don't understand you")
        engine.runAndWait()
        





Przycisk = Button(root, text = "Execute the command!", command=Recognize, width=20, height = 5)
Przycisk.pack(pady = 100)








mainloop()
