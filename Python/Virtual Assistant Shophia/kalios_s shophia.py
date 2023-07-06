import datetime
import os
import smtplib
import webbrowser

import pyttsx3 as p  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia

engine = p.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def shutdown():
    speak('understood sir')
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown /s /t 1')


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("Myself Laxmi , attitude girl, murder kr dungi ")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hindi-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
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

        elif 'open youtube' in query:
            speak('opening youtube...')
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            speak('opening google...')
            webbrowser.open("https://www.google.com")
        elif 'open whatsapp' in query:
            speak('opening whatsapp...')
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open facebook' in query:
            speak('opening facebook...')
            webbrowser.open("https://facebook.com")
        elif 'who made you' in query:
            speak('A wonderful creater named Kalios')
        elif 'do you love me' in query:
            speak('I love you as a friend')
        elif 'where do you live' in query:
            speak("help!, i am stuck inside a device")
        elif "what can i call" in query:
            speak("im kara your virtual assistant")
        elif "can" in query and "i" in query and "call you" in query:
            speak("you can but i love my original name given by my maker")
        elif (("i" in query and "am" in query) or "im" in query) and ("bored" in query or "bore" in query):
            speak("you can ask me to play some songs or i can tell you a joke")
        elif 'are you good or bad' in query:
            speak('I am just like you')
        elif 'I love you' in query:
            speak('sorry! i have a boyfriend')

        elif 'quit' in query:
            speak('have a nice day Sir...')
            os._exit()


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to receiver name' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "your email"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")
            except:
                speak("ooh some error occurred try again")
