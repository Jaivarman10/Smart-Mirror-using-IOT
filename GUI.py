import tkinter as tk
import time
import requests

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label_time.config(text=current_time)
    root.after(1000, update_time)
def get_weather():
    api_key = "a79fff33ba987adaf5769a2978d0b792"
    city = "Coimbatore"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    if response.get("weather"):
        weather_description = response["weather"][0]["description"]
        temperature = response["main"]["temp"] - 273.15
        label_weather.config(text=f"{city}: {weather_description}, {temperature:.1f}°C")
    else:
        label_weather.config(text="Error fetching weather data")
root = tk.Tk()
root.title("Smart Mirror")
label_time = tk.Label(root, font=("Helvetica", 48), fg="white", bg="black")
label_time.pack()
label_weather = tk.Label(root, font=("Helvetica", 24), fg="white", bg="black")
label_weather.pack()
update_time()
get_weather()
root.configure(bg='black')
root.attributes('-fullscreen', True)
root.mainloop()
