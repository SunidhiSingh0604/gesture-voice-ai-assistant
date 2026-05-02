
import os
from voice.tts import say

def open_app(query):
    if "notepad" in query:
        os.system("notepad")
        say("Opening Notepad")

    elif "calculator" in query:
        os.system("calc")
        say("Opening Calculator")
