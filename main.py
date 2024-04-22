import requests


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        print(f"Obecna pogoda w: {city}")
        print(f"Opis: {weather_description}")
        print(f"Temperatura: {temperature} °C")
        print(f"Wilgotność: {humidity}%")
        print(f"Predkosc wiatru: {wind_speed} m/s")
    else:
        print("Bład: ", data['message'])


api_key = "a5700603a72d9ceb9481e37a8c154e6b"
city='Warsaw'
get_weather(api_key,city)
