import subprocess
import datetime
import wolframalpha
import pyttsx3
import speech_recognition as sr 
import requests
from bs4 import BeautifulSoup 
import operator
import random
import json
import webbrowser 
import os
from twilio.rest import Client
import tkinter
import winshell
import smtplib
import feedparser
import ctypes
from urllib.request import urlopen
import win32com.client as wincl
import time
import shutil
from clint.textui import progress
import wikipedia
import requests
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
#can change the voice to male using [0]
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>= 12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    assname("quirl 1 point o")
    speak("im ur assistance ")
    speak("assname")
def usrname():
    speak("what can i call you ")
    uname = takecommand()
    speak("hello ,(uname)")
    columns =shutil.get_terminal_size().column
    print("............".center(columes))
    print("hello ", uname.center(columes))
    print("............".center(columes))
    speak("how can i help you")

def takecommand():
    r = sr.recogniser()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language = 'en-in')
        print(f"usersaid: {query}\n")

    except exception as e:
            print(e)
            print("unable to recognize your voice please! try again ")
            return "none"

    return query
# now the main function starts her now we will call it as a main function 
if '_name_' == '_mains_':
    clear = lambda: os.system('cls')
    clear()
    wishme()
    username()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia ...")
            query =query.replace("wikipedia","")
            speak("According to wikipedia")
            print(results)
            speak(result)
        elif 'open youtube' in query:
            speak("her you go to youtube")
            webbrowser.open("youtube.com")

        elif'open google' in query:
            speak("her you go to google")
            webbrowser.open("google.com")
             
        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            
        elif"how are you" in query:
            speak("i am fine ,thankyou")
            speak("how are you")
        elif" fine" in query:
            speak("its good to know that your fine ")

        elif("change  my name") in query:
            speak (" ok ,so what would i call you  ")
            query = query.replace (" change my name to " , "")
            asssname = query
        elif (" what is your  name") in query:
            speak("my friends call me")
            speak("assname")
        elif (" exit") in query:
            speak("thanks for giving me your precious time ! thankyou so much ")
            exit()
        elif (" who made you") in query:
            speak(" i was made by yashasvi sakure , the legend")





            




