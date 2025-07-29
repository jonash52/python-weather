from services.weather_api import fetch_weather
from services.excel import append_to_excel
import time



while True:
    result = fetch_weather()
    append_to_excel(result)
    time.sleep(5)