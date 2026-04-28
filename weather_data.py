
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# get coordinates for area
latitude = "37.410276"
longitude = "-79.054780"

def local_weather_data(lat, long):

    # The URL of the API endpoint
    url = f"https://api.weather.gov/points/{lat},{long}"

    # Sending the request
    response = requests.get(url)

    # Checking if the request was successful (Status Code 200)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code}")
        return

    hourly_forcast_url = data["properties"]["forecastHourly"]
    response_hourly = requests.get(hourly_forcast_url)
    hourly_data = response_hourly.json()

    hourly_df = pd.DataFrame(hourly_data["properties"]["periods"])

    def strip_fn(x):
        return float(x.replace("mph","").strip())

    hourly_df["windSpeed"] = hourly_df["windSpeed"].apply(strip_fn) 
    
    hourly_df["startTime"] = pd.to_datetime(hourly_df["startTime"])

    return hourly_df

df = local_weather_data(latitude, longitude)
