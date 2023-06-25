# AMAN
#imported liba=raries

import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pyaudio
import os
import pyjokes as pj
import requests
import json
import pyautogui
import random
import subprocess as sp

##password
passwordd="python"

###voice enabling
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()



###speech rec function        
def command():
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("I am Recognizing.....")
        Request = r.recognize_google(audio,language='en-in')
        print(f"you said : {Request} \n")
    except Exception as e:
            print(e)
            print("Sorry!! Say that again")
            return ""   
    
    return Request.lower()

##chatbot
Hello = ('hello','hey','hii','hi')

reply_Hello = ('Hello Sir , I Am gama .',
            "Hey , What's Up ?",
            "Hey How Are You ?",
            "Hello Sir , Nice To Meet You Again .",
            "Of Course Sir , Hello .")

Bye = ('bye','exit','sleep','go')

reply_bye = ('Bye Sir.',
            "It's Okay .",
            "It Will Be Nice To Meet You again .",
            "Bye.",
            "Okay.")

How_Are_You = ("how are you"
               ,'are you fine' , 'how r u')

reply_how = ('I Am Fine.',
            "Excellent .",
            "Moj Ho rhi Hai .",
            "Absolutely Fine.",
            "I'm Fine.",
            "Thanks For Asking.")

nice = ('nice','good','thanks')

reply_nice = ('Thanks .',
            "Ohh , It's Okay .",
            "Thanks To You.")

Functions = ['functions','abilities','what can you do','features']

reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks , How Can I Help You ?',
            'I Can Call Your G.F .',
            'I Can Message Your Mom That You Are Not Studing..',
            'I Can Tell Your Class Teacher That You Had Attended All The Online Classes On Insta , Facebbook etc!',
            'Let Me Ask You First , How Can I Help You ?')

sorry_reply = ("Sorry , That's Beyond My Abilities .",
                "Sorry , I Can't Do That .",
                "Sorry , That's Above Me.")

   #### starting voice initial 

def intro():
    speak("Hello I am your Voice Assistant , how may i help you")

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("good morning")
    elif hour<=18 and hour>=12:
        speak("goood afternoon")
    else:
        speak("Good night")


#OS FUNCTIONS
def open_cmd():
    sp.run('start microsoft.windows.command prompt:' , shell=True)

def open_notepad():
    sp.run('start microsoft.windows.notepad:' , shell=True)

def open_camera():
    sp.run('start microsoft.windows.camera:' , shell=True)

def open_powerpoint():
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

def open_calendar():
    sp.run('start microsoft.windows.calendar:' , shell=True)

def open_calculator():
    sp.run('start microsoft.windows.calculator:' , shell=True)

def open_word():
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

def open_vscode():
    os.startfile("D:\\Microsoft VS Code\\Code.exe")

def search_web(query):
    query=query.replace(" " , "+")
    search = f"https://www.google.com/search?q={query}"

def weather():
    apikey="7eb217f8051122380d09dbc253be4ef3"
    speak("please Enter your city")
    city=input("Enter your city :")
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7eb217f8051122380d09dbc253be4ef3"
    response=requests.get(url)
    data=response.json()
    print("Real Temperature is " , round(((data["main"]["temp"]) - 273),2))
    print("Temperature feels like" , round((data["main"]["feels_like"])-273,2))
    print("Minimum Temperature is" , round((data["main"]["temp_max"])-273,2))
    print("Maximum Temperature is" , round((data["main"]["temp_min"])-273,2))

if __name__=="__main__":
    speak("You Need Password To Access this")
    print("You Need Password To Access this")
    passwordd=input("Enter The Password : ")
    if passwordd=="python":
        speak("Access Granted")
        wishme()
        intro()
        
        while True:
            query = command()

            #chit chat functions

            if 'what' and 'name' in query:
                speak("my name is GAMA")

            elif query in Hello:

                reply = random.choice(reply_Hello)

                speak(reply)
        
            elif query in nice:

                reply = random.choice(reply_nice)

                speak(reply)

            elif query in Bye:

                reply = random.choice(reply_bye)

                speak(reply)
                break

            elif query in How_Are_You:

                reply_ = random.choice(reply_how)

                speak(reply_)

            elif query in Functions:

                reply___ = random.choice(reply_Functions)

                speak(reply___)

            elif 'created' in query:
                speak("My creators are manav , aparna , aman , aditya and gaurav")     

            elif 'hello' in query:
                speak("hello,how are you?")

            elif 'how are you' in query:
                speak("I am fine")

            elif 'i am fine' in query:
                speak("good. how can i help you?")

            elif 'i want help' in query:
                speak("yes,i am here to help you ")

            elif 'human' in query:
                speak("no i am a robot")

            elif 'what is your name' in query:
                speak("my name is gama")    

            elif 'favourite' and 'game' in query :
                speak("Minecraft")
            
            elif 'joke' in query:
                p=pj.get_joke(language="en" , category="neutral")
                print(p)
                speak(p)

            elif 'time' in query:
                time=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {time}")    

            #webiste openings

            elif 'youtube' in query:
                speak("Do you want me to search anything on youtube")
                speak("Say yes or no?")
                query=command()
                if 'yes' in query:
                    speak("what do you want to search")
                    query=command()
                    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                elif 'no' in query:
                    webbrowser.open("youtube.com")

                else:
                    speak("I didnt understand your response")
                    speak("Gooodbye , have a nice day sir")    

            elif 'google' in query:
                speak("Do you want me to search anything on google")
                speak("Say yes or no?")
                query=command()
                if 'yes' in query:
                    speak("what do you want to search")
                    query=command()
                    query=query.replace(" " , "+")
                    search = f"https://www.google.com/search?q={query}"
                    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                elif 'no' in query:
                    webbrowser.open("google.com")

                else:
                    speak("I didnt understand your response")
                    speak("Gooodbye , have a nice day sir")     


            elif 'netflix' in query:
                webbrowser.open("https://www.netflix.com")
                break

            elif 'hotstar' in query:
                webbrowser.open("https://www.hotstar.com")
                break

            elif 'order food' in query:
                speak("From where , would you like order")
                speak("Dominos Swiggy Zomato ")
                query=command()
                if 'zomato' in query:
                    webbrowser.open("https://www.zomato.com/")

                elif 'swiggy' in query:
                    webbrowser.open("https://www.swiggy.com/")

                elif 'dominos' in query:
                    webbrowser.open("https://www.dominos.co.in/")

                else:
                    speak("I didnt understand your response")
                    speak("Gooodbye , have a nice day") 
                break

            elif 'wikipedia' in query:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'myntra' in query:
                webbrowser.open("myntra.com")
                break

            elif 'flipkart' in query:
                webbrowser.open("flipkart.com")
                break

            elif 'amazon' in query:
                webbrowser.open("amazon.com")
                break

            elif 'resso' in query:
                webbrowser.open("resso.com")
                break

            elif 'whatsapp' in query:
                webbrowser.open("web.whatsapp.com")
                break


            #####os functions


            elif 'notepad' in query:
                open_notepad()

            elif 'command prompt' or 'cmd' in query:
                open_cmd()

            elif 'camera' in query:
                open_camera()

            elif 'calculator' in query:
                open_calculator()

            elif 'calendar' in query:
                open_calendar()

            elif 'word' in query:
                open_word()

            elif 'powerpoint' in query:
                open_powerpoint()

            elif 'vs code' in query:
                open_vscode()    

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak("Sir, the time is {strTime}")

            elif "search" in query:
                speak("What would you like me to search for?")
                query = command()
                search_web(query)

            elif 'weather' in query:
                weather() 

            elif "exit" in query:
                speak("Goodbye!")

            else:
                speak(random.choice(sorry_reply))
                speak("Have a nice day")
                break

    else:
        speak("Access denied")
        print("Access denied")
