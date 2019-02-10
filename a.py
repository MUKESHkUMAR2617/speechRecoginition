import win32com.client as wincl
import speech_recognition as sr
import re 
import webbrowser
import os
def speak(vk):

    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(vk)

def recordAudio():

    # Record Audio

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Say something!")

        audio = r.listen(source)

    data = ""

    try:

        data = r.recognize_google(audio)

        print("You said: " + data)

    except sr.UnknownValueError:

        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:

        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):

    if "how are you" in data:

        speak("I am fine")
    
    elif "where are you" in data:

         speak("i am in bhopal madhya pardesh")   

    elif 'open website' in data:
        reg_ex = re.search('open website (.+)', data)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            speak("website is open now")
            print('Done!')
        else:
            pass

    elif 'what\'s up' in data:
        speak('Just doing my thing')   
    elif 'open Notepad' in data:
        os.system('notepad.exe')    
    elif 'shutdown' in data:
        os.system('shutdown /s /t 1')
    elif 'restart'in data:
        os.system('shutdown /r /t 1') 
    else:
        speak(data)          
while 1:

        data = recordAudio()
        jarvis(data)
    