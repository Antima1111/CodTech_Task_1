import requests
import matplotlib.pyplot as plt
from datetime import datetime


API_KEY = "0014bad623cdca6bc1b627afc4f4f4ab" 
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"


response = requests.get(URL)
data = response.json()

if data["cod"] != "200":
    print("Failed to fetch data. Check your API key or city name.")
    exit()


dates = []
temperatures = []

for forecast in data["list"]:
    dt_txt = forecast["dt_txt"]
    temp = forecast["main"]["temp"]
    
    if "12:00:00" in dt_txt:
        dates.append(datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").date())
        temperatures.append(temp)

plt.figure(figsize=(10, 5))
plt.plot(dates, temperatures, marker='o', color='teal')
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()
