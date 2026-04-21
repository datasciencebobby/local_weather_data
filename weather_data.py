
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# get coordinates for area
latitude = "37.410276"
longitude = "-79.054780"

# The URL of the API endpoint
url = f"https://api.weather.gov/points/{latitude},{longitude}"

# Sending the request
response = requests.get(url)

# Checking if the request was successful (Status Code 200)
if response.status_code == 200:
    data = response.json()
    #print(data)
else:
    print(f"Error: {response.status_code}")

hourly_forcast_url = data["properties"]["forecastHourly"]
response_hourly = requests.get(hourly_forcast_url)
hourly_data = response_hourly.json()



hourly_df = pd.DataFrame(hourly_data["properties"]["periods"])
print(hourly_df.columns) 
print(hourly_df["windSpeed"].head(10))

def strip_fn(x):
    return float(x.replace("mph","").strip())

hourly_df["windSpeed"] = hourly_df["windSpeed"].apply(strip_fn) 

print(hourly_df["windSpeed"].head(10))
  
hourly_df["startTime"] = pd.to_datetime(hourly_df["startTime"])

#plt.plot(hourly_df["startTime"], hourly_df["temperature"])
plt.plot(hourly_df["startTime"], hourly_df["windSpeed"])
#plt.plot(hourly_df["probabilityOfPrecipitation"])

plt.show()
