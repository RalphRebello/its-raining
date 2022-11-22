import requests

API_KEY = "0fb5387f737872fedfc8bcdd2a9a3ad6"
CITY_NAME = "viamao"
LINK_API = (f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={CITY_NAME}&"
            f"appid={API_KEY}&"
            f"units=metric&"
            f"lang=pt_br")


def get_insta_weather():
    print("Instant Weather")
    local = requests.get(LINK_API)

    get_dic = local.json()
    description = get_dic['weather'][0]['description']
    temperature = get_dic['main']['temp']
    feels = get_dic['main']['feels_like']
    humidity = get_dic['main']['humidity']
    print(f'{description} | Real Temperature {temperature} | Feels Like: {feels} | Humidity: {humidity}')

