from tkinter import *  # it is used to create the GUI
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox, PhotoImage

from timezonefinder import TimezoneFinder
from datetime import datetime, time
from time import strftime  # Importing strftime directly
import requests
import pytz

from django.utils import timezone

root = Tk()  # this creates  new window and store it in root
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)  # it means window size cannot be changed by the user


def getWeather():
    city_name = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city_name)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    name1.config(text="Current Time :")
    # weather
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=dcdcef0d024cb39b966c6fd38d1c807f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp, "°"))
    c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)
    messagebox.showinfo("Weather Update", f"Weather in {city_name} has been updated successfully!")


# Here we implement the Search box
Search_image = PhotoImage(file="s.png")
myimage = Label(image=Search_image)  # this display the loaded image
myimage.place(x=20, y=20)  # these are the coordinate on the window
textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0,
                     fg="white")  # Here we implement the textfield
textfield.place(x=50, y=40)
textfield.focus()

# Here we implement the logo
Search_icon = PhotoImage(file="i.png")
logo = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
logo.place(x=400, y=34)

# Here is the logo
logo_image = PhotoImage(file="lo.png")
logo = Label(image=logo_image)
logo.place(x=100, y=120)

# Here we implement the bottom box
Frame_image = PhotoImage(file="bot.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)   #This is a way to arrange the container in the window.

#  Here we implement the time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=25, y=100)
name1 = Label(root, font=("arial", 15, "bold"), fg="red")  #root tell us this is our main window
name1.place(x=570, y=35)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=710, y=30)

# Here we implement the label
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 20, "bold"))
c.place(x=400, y=250)

# Here is the bottom label
w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=130, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=430, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=690, y=430)

root.mainloop()
