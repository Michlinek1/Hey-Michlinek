import random
import datetime
from tkinter import *
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
#niggersniggers hate niggers
def Feelings():
    Monday = (
        "I feel horible, because Monday has started",
        "Could be better",
        "It's monday, so as you might expect, I don't feel amazing",
        "Somehow I feel good",
        "I want to die"
    )
    Tuesday = (
        "It's ok",
        "I'm already thinking about the weekend",
        "It's amazing!"
        "I have a sore throat which means, I want to go back home",
    )
    Wednesday = (
        "Closer and closer to the weekend",
        "My friend beat me at the school",
        "I can already feel the weekend vibe",
        "In one word? Horible",
        "Don't ask me about that"
    )
    Thurdsay = (
        "I feel amazing, because weekend is in two days! ",
        "You know what? I don't want to answer to your question",
        "My mom gave ma a very harsh punishment, so I don't feel  good",
        "Kinda good, what about you?",
    
    )
    Friday = (
        "Finally it is friday!",
        "Even at friday i feel bad",
        "I feel AMAZING!"
        "Sadly, I'm ill"
        "I'm going out with my friends!"
    )
    Saturday = (
        "I'm so drunk!"
        "I'm still ill"
        "I feel good"
        "Closer and closer to the monday"
    )
    Sunday = (
        "Sadly tommorow i have to got to work"
        "My stomach hurts so much"
        "I'm still feeling great"
    )
    if datetime.datetime.today().strftime("%A") == "Monday":
        RandomMonday = random.choice(Monday)
        engine.say(RandomMonday)
        engine.runAndWait()  
    elif datetime.datetime.today().strftime("%A") == "Tuesday":
        RandomTuesday = random.choice(Tuesday)
        engine.say(RandomMonday)
        engine.runAndWait()
    elif datetime.datetime.today().strftime("%A") == "Wednesday":
        RandomWednesday = random.choice(Wednesday)
        engine.say(RandomWednesday)
        engine.runAndWait()
    elif datetime.datetime.today().strftime("%A") == "Thursday":
        RandomThursday = random.choice(Thurdsay)
        engine.say(RandomThursday)
        engine.runAndWait()
    elif datetime.datetime.today().strftime("%A") == "Friday":
        RandomFriday = random.choice(Friday)
        engine.say(RandomFriday)
        engine.runAndWait()
    elif datetime.datetime.today().strftime("%A") == "Saturday":
        RandomSaturday = random.choice(Saturday)
        engine.say(RandomSaturday)
        engine.runAndWait()
    elif datetime.datetime.today().strftime("%A") == "Sunday":
        RandomSunday = random.choice(Sunday)
        engine.say(RandomSunday)
        engine.runAndWait()
    
    


