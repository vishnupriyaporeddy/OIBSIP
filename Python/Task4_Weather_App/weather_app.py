
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            print("\n========== WEATHER REPORT ==========")
            print("City        :", data["name"])
            print("Temperature :", data["main"]["temp"], "°C")
            print("Condition   :", data["weather"][0]["description"])
            print("Humidity    :", data["main"]["humidity"], "%")
            print("Wind Speed  :", data["wind"]["speed"], "m/s")
            print("====================================")

        elif response.status_code == 404:
            print("City not found! Please check the city name.")

        elif response.status_code == 401:
            print("Invalid or inactive API key. Check your API key.")

        else:
            print("Unable to fetch weather data. Try again.")

    except requests.exceptions.RequestException:
        print("Network error! Please check your internet connection.")


print("====================================")
print("          WEATHER APP")
print("====================================")

if not API_KEY:
    print("API key not found! Please check your .env file.")
else:
    city = input("Enter city name: ").strip()

    if city:
        get_weather(city)
    else:
        print("Please enter a city name.")
