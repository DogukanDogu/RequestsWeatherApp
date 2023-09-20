import json
from tkinter.ttk import Combobox
import re
import requests
from tkinter import *


class City:
    name = ""
    coords = ""


response = requests.get("https://raw.githubusercontent.com/DogukanDogu/RequestsWeatherApp/main/Turkiye_Cities.json")

response.encoding = 'utf-8-sig'
data = json.loads(response.text)

cities = []

for res in data:
    City.name = res['Province']
    City.coords = res['Coordinates']
    cities.append(City.name + " " + City.coords)

window = Tk()
window.geometry("500x500")
window.title = "Weather App"
combo = Combobox(values=cities, width=100,font=("Arial", 18))
combo.pack()

label = Label(width=100)
label.pack()

global selected_option

def getWeatherData(latitude, longitude,countrycode, apikey):
    response = requests.get("https://pro.openweathermap.org/data/2.5/forecast/hourly?lat="
                            + str(latitude) + "&lon=" + str(longitude) + "&lang=" + countrycode + "&appid=" + apikey)
    return response.json()

def option_selected(event):
    selected_option = combo.get()
    label.config(text=selected_option, font=("Arial", 18))
    pattern = r'(\d+\.\d+),\s(\d+\.\d+)'

    match = re.search(pattern, selected_option)

    if match:
        latitude = match.group(1)
        longitude = match.group(2)
        weather_data = getWeatherData(latitude,longitude,"tr","")
        print(weather_data)
    else:
        print("Koordinatlar bulunamadi.")


combo.bind("<<ComboboxSelected>>", option_selected)

window.mainloop()
