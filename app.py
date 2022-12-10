# ======= Main Module Import ======
import pyttsx3
from time import ctime
import playsound
import speech_recognition as sr
import os

import wikipedia
import webbrowser

# ========= Services Module Import =====
from Services.Speech_control.speech_control import speak
from Services.Greeting.greeting import greet
from Services.Recognition.recognition import recognze

# ========= Features Module Import =====
from Features.Screenshot.screenshot import take_screenshot
from Features.Jokes.jokes import tell_me_joke
from Features.Date_time.date_time import date , time
from Features.Video_download.video_download import download_yt_video

# greet()
# recognze()

if __name__ == "__main__":
    # greet()
    # while True:
    if 1:
        query = recognze().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("Opening Youtube")
            print(f"Magic : Opening Youtube\n")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("Opening Google")
            print(f"Magic : Opening Google\n")
            webbrowser.open("google.com")
        
        elif 'screenshot' in query:
            take_screenshot(1)

        elif 'joke' in query:
            tell_me_joke()
        
        elif 'date' in query:
            date()

        elif 'time' in query:
            time()

        elif 'download video' in query:
            download_yt_video(1)
            