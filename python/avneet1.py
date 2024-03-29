import pyttsx3 #pip install pyttsx3
from googletrans import Translator
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit #pip install pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    # speak(f"Sir, the time is {strTime}")
    # speak("I am avneet kaur. Please tell me how may I help you")       
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('psthakkar2@gmail.com', '21502I.T@parth')
    server.sendmail('psthakkar2@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("say want you search")
            content = takeCommand()
            webbrowser.open('https://www.youtube.com/results?search_query=' +content)
            
        elif 'open 2' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'google' in query:
            speak("say want you search")
            content = takeCommand()
            webbrowser.open('https://www.google.co.in/?#q=' +content)                  

        elif 'open 1' in query:
            webbrowser.open("https://www.google.com/")     
    
        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'open gaana' in query:
            webbrowser.open("https://gaana.com/")

        elif 'open classroom' in query:
            webbrowser.open("https://classroom.zgoogle.com/u/0/h")

        elif 'open email' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open GitHub' in query:
            webbrowser.open("https://github.com/")

        elif 'open channel 1' in query:
            webbrowser.open("https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")

        elif 'open channel 2' in query:
            webbrowser.open("https://www.youtube.com/channel/UCStj-ORBZ7TGK1FwtGAUgbQ")

        elif 'open Data Science in python ' in query:
            webbrowser.open("https://www.youtube.com/watch?v=pF-h1YCS5GE&list=PLu0W_9lII9agK8pojo23OHiNz3Jm6VQCH-")

        elif 'open Django Course' in query:
            webbrowser.open("https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9")

        elif 'open Python Course' in query:
            webbrowser.open("https://www.youtube.com/watch?v=gfDE2a7MKjA&t=6031s")

        elif 'open Python Advance Course' in query:
            webbrowser.open("https://www.youtube.com/watch?v=61a7UkDO50s&t=3s")

        elif 'open HTML CSS and JS' in query:
            webbrowser.open("https://www.youtube.com/watch?v=6mbwJ2xhgzM&list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg")

        elif 'open Java Script' in query:
            webbrowser.open("https://www.youtube.com/watch?v=hKB-YGF14SY")

        elif 'open PHP' in query:
            webbrowser.open("https://youtube.com/playlist?list=PLbGui_ZYuhiihdSW-kg50d0L4or1DWvko")

        elif 'open WhatsApp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")

        elif 'what is my Google Password' in query:
            print("sir your Google Password is 21502I.T@parth")
            speak("sir your Google Password is 21502I.T@parth")

        elif 'what is my phone Password' in query:
            print("sir your phone Password is 2157")
            speak("sir your phone Password is 2157")    

        elif 'what is my laptop Password' in query:
            print("sir your laptop Password is parth21")
            speak("sir your laptop Password is parth21")

        elif 'what is my Google Password' in query:
            print("sir your Google Password is 21502I.T@parth")
            speak("sir your Google Password is 21502I.T@parth")

        elif 'what is my wifi Password' in query:
            print("sir your wif  Password is 2157I.T@parth")
            speak("sir your wifi Password is 2157I.T@parth")

        elif 'what is my git hub Password' in query:
            print("sir your git hub Password is 21502I.T@parth")
            speak("sir your git hub Password is 21502I.T@parth")

        elif 'what is my ms office Password' in query:
            print("sir your ms office Password is 21502I.T@parth")
            speak("sir your ms office Password is 21502I.T@parth")

        elif 'what is my outlook Password' in query:
            print("sir your outlook Password is dell1234")
            speak("sir your outlook Password is dell1234")

        elif 'what is my mcafee Password' in query:
            print("sir your mcafee Password is 21502I.T@parth")
            speak("sir your mcafee Password is 21502I.T@parth")

        elif 'what is my Programing guruji Password' in query:
            print("sir your Programing guruji Password is 21502I.T@parth")
            speak("sir your Programing guruji Password is 21502I.T@parth")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        #  elif 'none' in query:
        #  content = takeCommand()        

        elif 'open visual studio' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'avneet open time table' in query:
            codePath = "C:\\Users\\PARTH\\OneDrive\\Desktop\\sem 4 time table.jpeg"
            speak("opening time table")
            os.startfile(codePath)
            print("parth time table is opened")

        elif 'avneet open sem 3' in query:
            codePath = "E:\sal\SEM - 3"
            os.startfile(codePath)

        elif 'open sem 4' in query:
            codePath = "E:\sal\SEM - 4"
            os.startfile(codePath)

        elif 'close notepad' in query:
   
            codePath = "E:\sal\SEM - 4"
            os.system("taskkill/im notepad.exe")

        elif 'close browser' in query:
            codePath = "E:\sal\SEM - 4"
            os.system("taskkill/im chrome.exe")

        elif 'close app' in query:
            codePath = "E:\sal\SEM - 4"
            os.system("taskkill/im Code.exe")

        elif 'mummy' in query:
                speak("What should I say?")
                content = takeCommand()        
                pywhatkit.sendwhatmsg('+919173142133', content, 23, 40 )
            
        elif 'parth' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "psthakkar2@outlook.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my love parth. I am not able to send this email")    