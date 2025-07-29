import requests
from Config import Config



def fetch_weather():
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={Config.CITY}&appid={Config.API_KEY}"

    try:
        response = requests.get(URL)
        data = response.json()
        return data
    except:
        print("Błąd")

result = fetch_weather()

print(result)

# temp_min = convert_temp( result.get("main").get("temp_min"), "f" )
# pressure = result.get("main").get("pressure")
# feels_like = convert_temp( result.get("main").get("feels_like"), "c" )
#
# wind = result.get("wind").get("speed")
#
# print(temp_min)