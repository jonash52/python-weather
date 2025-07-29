import requests
from Config import Config
from tools.utils import convert_temp
from datetime import datetime

def fetch_weather():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={Config.CITY}&appid={Config.API_KEY}"

    try:
        response = requests.get(URL)
        data = response.json()
        weather = {
            "temp_min": convert_temp( data.get("main").get("temp_min"), "f" ),
            "pressure": data.get("main").get("pressure"),
            "feels_like": convert_temp( data.get("main").get("feels_like"), "c" ),
            "wind": data.get("wind").get("speed"),
            "city": data.get("name"),
            "timestamp": datetime.now().strftime("%H:%M:%S %d.%m.%y"),
            "lat" : data.get("coord").get("lat"),

        }
        return weather
    except:
        print("Błąd")