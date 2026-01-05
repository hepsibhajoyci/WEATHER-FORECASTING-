import requests
from tkinter import *
from tkinter import messagebox

# Function to get weather data
def get_weather():
    city = city_entry.get().strip()
    if city == "":
        city = "Delhi"  # Default city name
        messagebox.showinfo("Default City", "No city entered. Showing weather for Delhi.")
    
    # ✅ Replace with your actual OpenWeatherMap API key
    api_key = "YOUR_REAL_API_KEY"  # Example: "a1b2c3d4e5f6g7h8i9j0k1l2"
    
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?appid={api_key}&q={city}&units=metric"

    try:
        # Fetch data from API
        response = requests.get(complete_url)
        data = response.json()

        # Debugging line (optional)
        # print(data)

        # If response is valid
        if response.status_code == 200 and "main" in data:
            city_name = data.get("name", "N/A")
            country = data["sys"].get("country", "N/A")
            temperature = data["main"].get("temp", "N/A")
            humidity = data["main"].get("humidity", "N/A")
            weather_description = data["weather"][0].get("description", "N/A")

            result_label.config(
                text=f"🌆 City: {city_name}, {country}\n"
                     f"🌡 Temperature: {temperature}°C\n"
                     f"💧 Humidity: {humidity}%\n"
                     f"☁ Weather: {weather_description.capitalize()}"
            )
        elif data["cod"] == "404":
            messagebox.showerror("Error", "City not found. Please try again.")
        else:
            messagebox.showerror("Error", "Invalid API key or network issue.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# ---------------- GUI DESIGN ----------------

root = Tk()
root.title("🌦 Weather Forecast App")
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
Button(root, text="Get Weather", command=get_weather,
       bg="#1E90FF", fg="white", font=("Helvetica", 12, "bold"),
       relief="raised", cursor="hand2").pack(pady=10)

# Result label
result_label = Label(root, text="", font=("Helvetica", 12), bg="#87CEEB", justify=LEFT)
result_label.pack(pady=20)

# Run the GUI loop
root.mainloop()