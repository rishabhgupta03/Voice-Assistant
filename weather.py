import main
import requests
import json


def info(data):
    api_key = "a6b20a5000a5782be4dab5e6e39bbbf7"
    weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    data = data.split(" ")
    location = str(data[-1])
    url = weather_url + "appid=" + api_key + "&q=" + location
    js = requests.get(url).json()
    if js["cod"] != "404":
        weather = js["main"]
        temp = weather["temp"]
        hum = weather["humidity"]
        desc = js["weather"][0]["description"]
        resp_string = "in " + str(location) + " temperature in Kelvin is " + str(temp) + " The humidity is " + str(hum) + " and The weather description is "+ str(desc)
        main.respond(resp_string)
    else:
        main.respond("City Not Found")