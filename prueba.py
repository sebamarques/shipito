import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
print
listener = sr.Recognizer()
engine = pyttsx3.init()
escuchador = sr.Recognizer()
engine.say("trolito")
engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source:
                print("escuchando")
                voice = listener.listen(source)
                rec = listener.recognize_google(voice)
                print(rec) 
                if rec == "finish":
                        break
                while (rec == "shipito"):
                    print("entre")
                    voice = listener.listen(source)
                    rec1 = listener.recognize_google(voice)
                    print(rec1)
                    if rec1 == "YouTube":
                        webbrowser.open("https://www.youtube.com/",new=2,autoraise=True)
                    if rec1 == "twitch":
                        webbrowser.open("https://www.twitch.tv",new=2,autoraise=True)
                    if rec1 == "Twitter":
                        webbrowser.open("https://www.twitter.com",new=2,autoraise=True)
    except:
        print(".")