import tkinter as tk
from tkinter import ttk
import requests

# Fungsi untuk mendapatkan data cuaca berdasarkan nama kota dari Weatherstack API
def get_weather():
    api_key = "9fcef865b55b7d1aa2a8e9eec609a8df"  # Ganti dengan API key Anda
    city_name = city_entry.get()
    base_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city_name}"

    response = requests.get(base_url)
    data = response.json()

    if "current" in data:
        weather_description = data["current"]["weather_descriptions"][0]
        temperature_celsius = data["current"]["temperature"]
        humidity = data["current"]["humidity"]

        result_label.config(text=f"Cuaca di {city_name}:\n"
                                  f"{weather_description.capitalize()}\n"
                                  f"Suhu: {temperature_celsius:.2f}°C\n"
                                  f"Kelembaban: {humidity}%")
    else:
        result_label.config(text=f"Gagal mendapatkan cuaca di {city_name}!")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Cuaca")

# Frame utama
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)

# Label dan input untuk nama kota
city_label = ttk.Label(main_frame, text="Masukkan nama kota:")
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = ttk.Entry(main_frame)
city_entry.grid(row=0, column=1, padx=10, pady=10)

# Tombol untuk mendapatkan cuaca
get_weather_button = ttk.Button(main_frame, text="Dapatkan Cuaca", command=get_weather)
get_weather_button.grid(row=0, column=2, padx=10, pady=10)

# Label untuk hasil cuaca
result_label = ttk.Label(main_frame, text="", font=("Helvetica", 14))
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
