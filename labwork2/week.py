import requests
city = "Moscow,RU"
appid = "7cbce286d63148cd9f7eb4e14ed4e6e0"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': 'Moscow', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("Видимость:", i['visibility'], "метров")
    print("Скорость ветра:", i['wind']['speed'], "м/сек")
    print("________")