import requests
import os
import pytz
import pandas as pd
from datetime import datetime
from current_weather import CurrentWeather


params = {
    'lat': os.environ.get('lat'),
    'lon': os.environ.get('lon'),
    'appid': os.environ.get('api_key'),
    'units': 'metric'
}

response = requests.get(
    'https://api.openweathermap.org/data/2.5/weather',
    params=params
)

data = response.json()

eastern = pytz.timezone('America/New_York')
obs = {
    'lat': params['lat'],
    'lon': params['lon'],
    'units': params['units'],
    'dt': datetime.utcfromtimestamp(data['dt']).replace(tzinfo=pytz.utc).astimezone(eastern),
    'weather': data['weather'][0]['main'],
    'temp': data['main']['temp'],
    'wind_speed': data['wind']['speed'],
    'wind_deg': data['wind']['deg'],
    'visibility': data['visibility'],
    'sunset': datetime.utcfromtimestamp(data['sys']['sunset']).replace(tzinfo=pytz.utc).astimezone(eastern)
}

weather = CurrentWeather(**obs)
weather.print_weather()


df = pd.DataFrame([obs])
log_path = os.environ.get('weather_log_path')
if os.path.exists(log_path):
    df.to_csv(log_path, mode='a', header=False, index=False)
    print('Observation appended to log')
else:
    df.to_csv(log_path, mode='w', header=True, index=False)
    print('Observation log created')
