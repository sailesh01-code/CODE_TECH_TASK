import requests
import matplotlib.pyplot as plt
API_KEY = 'a386b5254ccf683fa6f100e76548f186'
CITY = 'Chennai'
url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"  
response = requests.get(url)
data = response.json()
if response.status_code != 200 or 'list' not in data:
    print("Failed to fetch weather data. Please check the API key or city name.")
    exit()
dates = []
temps = []
wind_speeds = []
pressures = []
conditions = []

for forecast in data['list']:
    try:
        dates.append(forecast['dt_txt'])
        temps.append(forecast['main']['temp'])
        wind_speeds.append(forecast['wind']['speed'])
        pressures.append(forecast['main']['pressure'])
        conditions.append(forecast['weather'][0]['main'])  
    except KeyError:
        continue
def reduce_labels(x, step=4):
    return [label if i % step == 0 else "" for i, label in enumerate(x)]
plt.figure(figsize=(12, 6))
plt.plot(dates, temps, label='Temperature (°C)', color='orange', marker='o')
plt.plot(dates, wind_speeds, label='Wind Speed (m/s)', color='blue', marker='x')
plt.xticks(ticks=range(len(dates)), labels=reduce_labels(dates), rotation=45)
plt.title(f"Weather Forecast - {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()
plt.figure(figsize=(12, 5))
plt.bar(dates, pressures, color='green')
plt.xticks(ticks=range(len(dates)), labels=reduce_labels(dates), rotation=45)
plt.title(f"Atmospheric Pressure Forecast - {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Pressure (hPa)")
plt.tight_layout()
plt.show()
print("\nWeather Conditions by Time:")
for d, c in zip(dates, conditions):
    print(f"{d} → {c}")