
import webbrowser
from voice.tts import say

def open_website(query):
    if "youtube" in query:
        webbrowser.open("https://youtube.com")
        say("Opening YouTube")

    elif "google" in query:
        webbrowser.open("https://google.com")
        say("Opening Google")
