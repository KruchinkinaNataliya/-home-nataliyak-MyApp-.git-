import requests
city = "Moscow,RU"
appid = "7cbce286d63148cd9f7eb4e14ed4e6e0"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params = {'q': 'Moscow', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", 'Moscow')
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Видимость:", data['visibility'], "метров")
print("Скорость ветра:", data['wind']['speed'], "м/сек")