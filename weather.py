import requests
from typing import Final

TOKEN: Final = '0cb696c928058acd17f8cc1d3b5caabf'
URL: str = 'https://api.openweathermap.org/data/2.5/weather'

def weather_api_handler(args: list) ->str:
    processed_list: list = []
    result:str = ''

    for i in args:
        i_lower = i.lower()
        processed_list.append(i_lower)

    result = str(get_weather_json(processed_list[0]))
    return result

def get_weather_json(name_of_city: str) ->dict:
    result: str = ''
    try:
        r = requests.get(URL, params={
            'q': name_of_city,
            'appid': TOKEN,
            'units': 'metric'
        })
    except:
        print(requests.ConnectionError)

    result = r.json()
    return result

