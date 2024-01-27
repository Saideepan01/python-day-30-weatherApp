from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

# *********************************** URL API
url_api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file = 'weather.key'
file_a = ConfigParser()
file_a.read(api_file)
api_key = file_a['api_key']['key']

def weather_find(city):
    final = requests.get(url_api.format(city, api_key))
    if final:
        json_file = final.json()
        city = json_file['name']
        country_name = json_file['sys']['country']
        k_temperature = json_file["main"]['temp']
        c_temperature = k_temperature-273.15
        f_temperature = (k_temperature-273.15)*9/5+32
        weather_display = json_file['weather'][0]['main']
        result = (city, country_name, c_temperature,f_temperature,weather_display)

        return result
    else:
        return None
def print_weather():
    city = search_city.get()
    weather = weather_find(city)
    if weather:
        location_entry['text'] = '{}, {}'.format(weather[0],weather[1])
        temperature_enntry['text'] = '{:.2f} C, {:.2f} F'.format(weather[2],weather[3])
        weather_entry['text'] = weather[4]

    else:
        messagebox.showerror('Error', 'Please enter a valid city name because it can not find')







#****************************** Size of App
root = Tk()
root.title("Weather App")
root.config(background="black")
root.geometry("700x400")

#*********************************** Search Space

search_city = StringVar()

enter_city = Entry(root, textvariable=search_city, fg="blue", font=("Arial", 30, "bold"))
enter_city.pack()

#************************************** Search Button
search_button = Button(root, text='Search Weather!', width=20, bg="red", fg="white", font=("Arial",25,"bold"), command=print_weather)
search_button.pack()

# *******************  OUTPUT OF CITY lOCATION OF PARTICULAR CITY
location_entry = Label(root, text='',bg="lightblue", font=("Arial",35,"bold"))
location_entry.pack()
# *************************** Temperature

temperature_enntry = Label(root, text='', font=("Arial", 35, "bold"), bg= "lightpink")
temperature_enntry.pack()

# *************************** Weather Entry
weather_entry = Label(root, text='',font=("Arial",35,"bold"),bg="lightgreen")
weather_entry.pack()




root.mainloop()
