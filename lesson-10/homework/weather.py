import requests

API_KEY = "a320ee6ee926068c59fc66db292fa52c"
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
weather_desc = data["weather"][0]["description"]
wind_speed = data["wind"]["speed"]
print(f"Weather in {CITY}:")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Condition: {weather_desc.capitalize()}")
print(f"Wind Speed: {wind_speed} m/s")