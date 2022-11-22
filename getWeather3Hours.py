import requests

API_KEY = "0fb5387f737872fedfc8bcdd2a9a3ad6"
CITY_NAME = "viamao"


def get_3_hours_weather():
    print("\nEvery 3 hours")
    local2 = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?"
                          f"q={CITY_NAME}&"
                          f"appid={API_KEY}&"
                          f"units=metric&"
                          f"lang=pt_br")

    get_dic = local2.json()
    for i in range(0, 8):
        description = get_dic['list'][i]['weather'][0]['description']
        temperature = get_dic['list'][i]['main']['temp']
        feels = get_dic['list'][i]['main']['feels_like']
        humidity = get_dic['list'][i]['main']['humidity']
        hours = get_dic['list'][i]['dt_txt']
        print(f'{description} | temp {temperature} | Feels {feels} | Hmd {humidity} | Time {hours}')

