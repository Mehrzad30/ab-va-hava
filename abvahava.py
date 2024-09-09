import requests

api_key = "58c4985f734828c66cea872a0018d3a6"
city_name = "Bandar Abbas"
country_code = "IR"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    main = data['main']
    wind = data['wind']
    weather = data['weather'][0]

    temperatrue = main['temp']
    weather_description = weather['description']
    wind_speed = wind['speed']

    print(f"shar: {city_name}")
    print(f"dma: {temperatrue}°c")
    print(f"vaziat hva: {weather_description}")
    print(f"sorat bad {wind_speed}متر بر ثانیه")
else:
    print("faild")