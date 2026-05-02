
import requests
from voice.tts import say
from config.settings import WEATHER_API_KEY

def get_weather():
    city = "Delhi"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    try:
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        say(f"{temp} degree with {desc}")

    except:
        say("Weather error")
