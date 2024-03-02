from utils import mps_to_kts


class CurrentWeather:
    def __init__(self, lat, lon, units, dt,
                 weather, temp, wind_speed, wind_deg,
                 visibility, sunset):
        self.lat = lat
        self.lon = lon
        self.units = units
        self.dt = dt
        self.weather = weather
        self.temp = temp
        self.wind_speed = wind_speed
        self.wind_deg = wind_deg
        self.visibility = visibility
        self.sunset = sunset

    def print_weather(self):
        print(self.dt.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
        print(f"Weather State: {self.weather}")
        print(f"Temp: {self.temp}°C")
        print(f"Wind Speed: {mps_to_kts(self.wind_speed)}kn")
        print(f"Wind Direction: {self.wind_deg}")
        print(f"Visibility: {self.visibility}m")
        print(f"Sunset: {self.sunset.strftime('%H:%M:%S')}")
        print()
