import requests
import json
city = input("Write the city name to find the temperature in celcius:  ")
api_key = "Put your own api key here"
base_url = 'http://api.openweathermap.org/data/2.5/weather'

parameter = {
    'q' : city,
    'appid' : api_key,
    'units': 'metric'
}

response = requests.get(base_url,params = parameter)

if response.status_code == 200:
    print("Request succesful! ")
else:
    f"Error: {response.status_code}"



weather_data = response.json()
temperature = weather_data['main']['temp']

print(f"The temperature in {city} is {temperature} °C ")