import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)


def takeCommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        audio=r.listen(source)
    
    try:
        
        print("Recognising..........")
        querry=r.recognize_google(audio,language="en-in")
        print("User Said:{}".format(querry))
        
    except Exception as e:
        
        print("Not be able to listen Say that again please!")
        return "None"
    return querry
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
        
    elif hour>=12 and hour<18:
        speak("Good afternoon Sir!")
        
    else:
        speak("Hii,Good Evening Sir!")
    speak("Im your assisstant, How may i help you Shariq Sir")
    

if __name__ == "__main__":
    wishMe()
    
    while True:
        querry=takeCommand().lower()
        
        if "wikipedia" in querry: 
            
            querry=querry.replace("wikipedia","")
            speak("Searching in Wkipedia for"+querry)
            results = wikipedia.summary(querry,sentences=2)
            speak(results)
            print(results)
            
        elif "shutdown" in querry:
            speak("Shutting Down the Program")
            print("Shutting Down the program")
            break
        
        elif "open youtube" in querry:
            speak('Opening Youtube.....')
            webbrowser.open("https://www.youtube.com")
            
        elif "open google" in querry:
            speak("opening google......")
            webbrowser.open("https://www.google.com")
            
        elif "open code" in querry:
            speak("Opening Visual Studio Code........")
            codepath="C:\\Users\\KHAN SHARIQ\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)
        
        elif "time" in querry:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is:{time}")
            print("The time is:",time)