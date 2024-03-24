from dotenv import load_dotenv
from pprint import pprint
import requests
import os


load_dotenv()


def get_current_weather(city="Melbourne"):

   requests_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

   weather_data = requests.get(requests_url).json()

   return weather_data

if __name__=="__main__":
    print('\n*** Get Current weather Conditions ***\n')
    city = input('\n Please enter a city name:')

    # check for empty strigs or strigs with only spaces

    if not bool(city.strip()):
        city="Melbourne"

    weather_data = get_current_weather(city)

    print ("\n")
    pprint(weather_data)


