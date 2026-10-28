"""
Day 12 · Task 2: requests library

Call a free API (e.g. Open-Meteo weather) with params, check response.status_code, parse .json().

Complete every TODO, run the file, and tick this task on the tracker.
"""
# pip install requests
import requests

URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 19.99,     # Nashik
    "longitude": 73.79,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "Asia/Kolkata",
    "forecast_days": 3,
}

# TODO 1: response = requests.get(URL, params=params, timeout=10)
# TODO 2: if response.status_code != 200, print the error and stop
# TODO 3: data = response.json(); print each day's date, max and min temperature
