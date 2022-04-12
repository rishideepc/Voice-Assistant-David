import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import random 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else: 
        speak("Good Evening Sir!")

    speak("I'm David, your personal assistant. How do I help?")

def listen():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("...")
        print("...")
        r.energy_threshold = 800
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        #print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User says: {query}\n")

    except Exception as e:
        # print(e)    
        #print("Say that again please...")
        speak("Could you say that again please...")
        return "None"
    return query


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening...")
        r.energy_threshold = 800
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')

    except Exception as e: 
        print("Could you say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
           
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia, ")
            print(results)
            speak(results)
        
        elif 'David, you up' in query:
            speak("Always at your service Sir! ")

        elif 'you up' in query:
            speak("Always at your service Sir! ")


        elif 'bored' in query:
            speak("Have you considered taking a walk Sir?")

        elif 'board' in query:
            speak("Have you considered taking a walk Sir?")

        elif 'bod' in query:
            speak("Have you considered taking a walk Sir?")
        
        elif 'something else' in query:
            speak("Shall I play some music Sir? ")
            ret=takeCommand().lower()
            if 'ok' in ret:
                music_dir = 'C:\\Users\\HP\\Documents\\MySongs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[4]))

            elif 'yes' in ret:
                music_dir = 'C:\\Users\\HP\\Documents\\MySongs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[5]))

        

        elif 'hello' in query:
            wishMe()

        elif 'Hello David' in query:
            wishMe()

        elif 'hello David' in query:
            wishMe()

        elif 'hello david' in query:
            wishMe()
        
        elif 'Hello david' in query:
            wishMe()


        elif 'open youtube' in query:
            speak("Sure Sir!")
            webbrowser.open("youtube.com")
            
        elif 'launch youtube' in query:
            speak("Sure Sir!")
            webbrowser.open("youtube.com")    

        elif 'open google' in query:
            speak("Sure Sir!")
            webbrowser.open("google.com")
            
        elif 'launch google' in query:
            speak("Sure Sir!")
            webbrowser.open("google.com")

        elif 'open wikipedia' in query:
            speak("Sure Sir!")
            webbrowser.open("wikipedia.org")
            
        elif 'launch wikipedia' in query:
            speak("Sure Sir!")
            webbrowser.open("wikipedia.org")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\Documents\\MySongs'
            songs = os.listdir(music_dir)
            print(songs)
            n = random.randint(0, 9) 
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'play some music' in query:
            music_dir = 'C:\\Users\\HP\\Documents\\MySongs'
            songs = os.listdir(music_dir)
            print(songs)
            n = random.randint(0, 9) 
            os.startfile(os.path.join(music_dir, songs[n]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'quit' in query:
            speak("Thank You Sir! You have a nice day.")
            exit()

        elif 'quick' in query:
            speak("Thank You Sir! You have a nice day.")
            exit()

        elif 'open the code editor' in query:
            codePath='C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        elif 'open code editor' in query:
            codePath='C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        elif 'open VS code' in query:
            codePath='C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
            
        elif 'launch VS code' in query:
            codePath='C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        
        elif 'launch chrome' in query:
            codePath1='C:\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(codePath1)

        elif 'launch opera' in query:
            codePath2='C:\\Users\\HP\\AppData\\Local\\Programs\\Opera\\launcher.exe'
            os.startfile(codePath2)

        elif 'launch Opera' in query:
            codePath2='C:\\Users\\HP\\AppData\\Local\\Programs\\Opera\\launcher.exe'
            os.startfile(codePath2)   

        elif 'open CAD software' in query:
            codePath3='C:\Program Files (x86)\LibreCAD\LibreCAD.exe'
            os.startfile(codePath3)

        elif 'open the CAD software' in query:
            codePath3='C:\Program Files (x86)\LibreCAD\LibreCAD.exe'
            os.startfile(codePath3)

        elif 'open cad software' in query:
            codePath3='C:\Program Files (x86)\LibreCAD\LibreCAD.exe'
            os.startfile(codePath3)

        elif 'open the cad software' in query:
            codePath3='C:\Program Files (x86)\LibreCAD\LibreCAD.exe'
            os.startfile(codePath3)

        elif 'launch CAD software' in query:
            codePath3='C:\Program Files (x86)\LibreCAD\LibreCAD.exe'
            os.startfile(codePath3)

        elif 'launch the CAD software' in query:
            codePath3='C:\Program Files (x86)\LibreCAD\LibreCAD.exe'
            os.startfile(codePath3)

        elif 'launch cad software' in query:
            codePath3='C:\Program Files (x86)\LibreCAD\LibreCAD.exe'
            os.startfile(codePath3)

        elif 'launch the cad software' in query:
            codePath3='C:\Program Files (x86)\LibreCAD\LibreCAD.exe'
            os.startfile(codePath3)

        elif 'send a text to Mom' in query:
            speak("What do you want send Sir?")
            ans=takeCommand().lower()
            speak("When do you want to send the message Sir?")
            print("hour")
            ans1=takeCommand().lower()
            print("minute")
            ans2=takeCommand().lower()
            pywhatkit.sendwhatmsg('+91 xxxxxxxxxx', ans , ans1, ans2)

        elif 'send a text to --whoever--' in query:
            speak("What do you want send Sir?")
            ans=takeCommand().lower()
            speak("When do you want to send the message Sir?")
            print("hour")
            ans1=takeCommand().lower()
            print("minute")
            ans2=takeCommand().lower()
            pywhatkit.sendwhatmsg('+91 xxxxxxxxxx', ans , ans1, ans2)

        elif 'thank you' in query:
            speak("Always a pleasure Sir.")

        
