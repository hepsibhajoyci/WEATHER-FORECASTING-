import requests
from tkinter import *
from tkinter import messagebox

# Function to get weather data
def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return
    
    # Replace with your own OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"

    # Fetching data from API
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]

        result_label.config(text=f"City: {city_name}, {country}\n"
                                 f"Temperature: {temperature}°C\n"
                                 f"Humidity: {humidity}%\n"
                                 f"Weather: {weather_description.capitalize()}")
    else:
        messagebox.showerror("Error", "City not found. Please enter a valid city name.")

# Creating main window
root = Tk()
root.title("Weather Forecast App")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="#87CEEB")

# Title label
Label(root, text="🌤 Weather Forecast", font=("Helvetica", 16, "bold"), bg="#87CEEB").pack(pady=10)

# City entry
Label(root, text="Enter City Name:", font=("Helvetica", 12), bg="#87CEEB").pack(pady=5)
city_entry = Entry(root, width=30, font=("Helvetica", 12))
city_entry.pack(pady=5)

# Search button
Button(root, text="Get Weather", command=get_weather, bg="#1E90FF", fg="white", font=("Helvetica", 12, "bold")).pack(pady=10)

# Result label
result_label = Label(root, text="", font=("Helvetica", 12), bg="#87CEEB", justify=LEFT)
result_label.pack(pady=20)

# Run the GUI loop
root.mainloop()
0