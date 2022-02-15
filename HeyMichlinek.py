from tkinter import *
from main import *
import speech_recognition as sr


sr = sr.Recognizer()
def Recognize():
    try:
        with sr.Microphone() as source:
            voice = sr.listen(source)
            command = sr.recognize_google(voice)
            cos = Label(root, text = command)
            cos.pack()
        
    except:
        pass

