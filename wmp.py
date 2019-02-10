import win32com.client as wincl
import speech_recognition as sr
import re 
import os
import pygame
import wave
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

    elif 'open vlc MediaPlayer' in data:
        vlc.MediaPlayer('c:///ProgramFile(*86)/VideoLan/vlc.mp3&') 
    elif 'open Windows Media Player' in data:
         os.system('Windows Media Player.wave&')
    elif 'open groove music' in data:
         os.system('Groove music.wave&') 
    elif 'open Notepad' in data:
         os.system('notepad.exe')               
    else:
        speak(data)          
while 1:

        data = recordAudio()
        jarvis(data)
  