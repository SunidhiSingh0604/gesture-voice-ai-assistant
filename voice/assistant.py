
import datetime

from voice.speech import take_command
from voice.tts import say
from features.weather import get_weather
from features.browser import open_website
from features.apps import open_app
from utils.state import gesture_active, program_running

def run_voice_assistant():
    say("Voice and gesture activated")

    while program_running.is_set():
        query = take_command()

        if not query:
            continue

        if "activate mouse" in query:
            gesture_active.set()

        elif "deactivate mouse" in query:
            gesture_active.clear()

        elif "exit" in query:
            program_running.clear()

        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            say(current_time)

        elif "weather" in query:
            get_weather()

        elif "open" in query:
            open_website(query)
            open_app(query)
