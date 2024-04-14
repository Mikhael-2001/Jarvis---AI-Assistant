import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # Wishes the user according to the time with the use of an if else loop
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning. Don't forget your daily cup of coffee!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon. Remember to complete your daily tasks for today!")

    else:
        speak("Good Evening. Don't stay up too long!")

    speak("I am Alexis, your personal assistant. What should I do for you?")


def takeCommand():
    '''
It takes the audio input from the user, analyzes it, and returns the required output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        ##print(e)
        print("Can you say that again, please?")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mikhaelangel2001@gmail.com', '10Messiislegend10')
    server.sendmail('mikhaelangel2001@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        #This is the logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("These are your results. According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'open my mail' in query:
            webbrowser.open("www.gmail.com")

        elif 'open Netflix' in query:
            webbrowser.open("https://www.netflix.com/browse")

        elif 'play music' in query:
            music_dir = 'C:\\Songs'
            Songs = os.listdir(music_dir)
            print(Songs)
            os.startfile(os.path.join(music_dir, Songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open Utorrent' in query:
            codePath = "C:\\Users\\mikha\\AppData\\Roaming\\uTorrent\\uTorrent.exe"
            os.startfile(codePath)

        elif 'open Visual Studio' in query:
            codePath = "C:\\Users\\mikha\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        elif 'open Teams' in query:
            codePath = "C:\\Users\\mikha\\AppData\\Local\\Microsoft\\Teams"
            os.startfile(codePath)

        elif 'send an email' in query:
            try:
                speak("What do you want me to send?")
                content = takeCommand()
                to = "komalthakur2312@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent succesfully!")
            except Exception as e:
                print(e)
                speak("Sorry, I was not able to send this email at the moment!")

        elif 'open linkedin' in query:
            webbrowser.open("www.linkedin.com")

        elif 'open udemy' in query:
            webbrowser.open("www.udemy.com")