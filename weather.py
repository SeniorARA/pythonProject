import requests
from typing import Final

#Static Variables
TOKEN: Final = '0cb696c928058acd17f8cc1d3b5caabf'
URL: str = 'https://api.openweathermap.org/data/2.5/weather'


#Main Api Handler Method
def weather_api_handler(args: list) ->str:
    processed_list: list = []
    # result: str = ''
    # json: dict = {}

    for i in args:
        i_lower = i.lower()
        processed_list.append(i_lower)

    json: dict = get_weather_json(processed_list[0])
    result: str = json_to_string_converter(json)

    return result


#Json Recipient Method
def get_weather_json(name_of_city: str) ->dict:
    # result: str = ''
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


#Json Converter(dict -> str) Method
def json_to_string_converter(json: dict) ->str:
    # result:str = ''
    template: str = '{} \nCity : {} \nTemperature : {} \nWind speed : {}'

    name: str = json['name']
    temp: float = json['main']['temp']
    wind_speed: int = json['wind']['speed']
    description: str = json['weather'][0]['description']



    result = template.format(description, name, str(temp), str(wind_speed))
    return result


