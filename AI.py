from urllib.request import DataHandler
import os
import time
from pygame import mixer
import pyttsx3
import speech_recognition as sr
import pyjokes
import pyautogui as pg
import webbrowser
import datetime
import requests
import wikipedia
x=datetime.datetime.now()
y=x.hour



def takeCommand():

    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")

            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def speak(audio):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate',150)

    engine.setProperty('voice', voices[0].id)
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()

def tellDay():

    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
def minwindow():
    pg.getWindowsWithTitle("Python")[0].minimize()
def maxwindow():
    pg.getWindowsWithTitle("Python")[0].maximize()

def song():
    speak("No music available at this moment")
    # mixer.init()
    # mixer.music.load(r'C:\Users\Marvan Babar\Music\Pareshan-Ho-Kay-Sanam-Marvi.mp3')
    # mixer.music.play()



def tellTime():
    x=datetime.datetime.now()
    y=x.hour
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
def forecast():
    city="Hyderabad"
    Api_Key="09ce12f3b75156894acbbc03a5b47b04"
    final_URL="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,Api_Key)
    result=requests.get(final_URL)
    data=result.json()
    temperature=data['main']['temp']
    wind=data['wind']['speed']
    windi=data['wind']['deg']
    cloudy=data['clouds']['all']
    temperature=temperature-273
    temperature=round(temperature,2)
    speak(f"Weather around you is {temperature} degree celsius. wind is at a speed of {wind} kilometer per hour and  at {windi} degrees. clouds are at {cloudy} percentage")
def joke():
    speak(pyjokes.get_joke())
def dateo():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)
def hello():

    
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    if y > 4 and y < 12:
        speak("Good Morning Zamal sir")
    elif y > 12 and y < 18:
        speak("Good Afternoon Zamal sir")
    elif y >= 18 and y <20 :
        speak("Good Evening Zamal sir")
    else:
        speak("Nothing")
    speak("Welcome back")
    # isd=datetime.datetime.now().strftime("%H:%M:%p")
    # std=isd.replace(":"," ")
    # speak(f"Its {std}")
    # forecast()

hello()
def Take_query():
    while(True):
        
        query = takeCommand().lower()
        if "open youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        elif "day" in query:
            tellDay()
            continue
        elif "time" in query:
            tellTime()
            continue
        elif "visual studio code" in query:
            os.startfile("C:\Users\Zamal Ali\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code")
        elif "creator" in query:
            speak("Zamal sir has brought me into existence")
        elif 'date' in query:
            dateo()
        # elif 'volume up' in query:
        #     pg.press("volumeup")
        # elif 'volume down' or 'reduce volume' in query:
        #     pg.press("volumedown")
        # elif 'mute' in query:
        #     pg.press("volumemute")
        elif "weather" in query:
            forecast()
        elif "joke" in query:
            speak("Here's a joke for you")
            joke()
            speak("Hahahahah")
        elif 'minimise' in query:
            minwindow()
        elif 'minimise' in query:
            maxwindow()
        elif "thank you" in query:
            speak("Always at your service sir")
        elif "wikipedia" in query:
            speak("Checking wikipedia now ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)
        elif "who are you" in query:
            speak("I am Ben. Your desktop Assistant. I was developed by Zamal sir using artificial intelligence")
        elif 'song' in query:
            speak("Songs are forbidden in Islam. I suggest you to listen to the soothing poetry of Allama Iqbaal")
            song()
        elif 'wait' in query:
            (speak("How much time"))
            n=int(input(Take_query()))
            print(n)
            time.sleep(n)
            
        elif 'sleep' in query:
            speak("As you command sir")
            exit()
        else:
            speak("You asked something beyond my knowledge")

if __name__ == '__main__':
    x=datetime.datetime.now()
    y=x.hour
    
    # main method for executing
    # the functions
    Take_query()
