import os
import time
import sys

def Installing():
    with open("requirements.txt", "r") as f:
        x = f.read()
        print(f"Reguired Dependences:\n{x}")

    try:
        import speech_recognition as sr
        import pyttsx3
        import pywhatkit
        import datetime
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        from translate import Translator
        from langdetect import detect, DetectorFactory
    except ImportError:
        os.system("pip install -r requirements.txt")
        print("Program reset is required!")
        time.sleep(1)
        sys.exit()


    




