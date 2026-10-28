"""
Day 18 · Task 1 · Build: weather CLI (typed & tested)

Then add a --explain flag that asks your LLM to describe the forecast in one friendly sentence.

Complete every TODO, run the file, then tick this task on the tracker.
"""
"""Weather CLI: typed, tested, with secrets in .env. Run: python day08/weather_cli.py Nashik"""
import sys

import requests
from pydantic import BaseModel


class DayForecast(BaseModel):
    date: str
    t_max: float
    t_min: float


CITIES = {"Nashik": (19.99, 73.79), "Pune": (18.52, 73.86), "Mumbai": (19.08, 72.88)}


def get_forecast(city: str, days: int = 3) -> list[DayForecast]:
    # TODO: look up lat/lon, call Open-Meteo (see day14), build DayForecast objects
    pass


def format_forecast(city: str, forecast: list[DayForecast]) -> str:
    # TODO: return a nice multi-line string. (Easy to test, no network!)
    pass


if __name__ == "__main__":
    city = sys.argv[1] if len(sys.argv) > 1 else "Nashik"
    print(format_forecast(city, get_forecast(city)))

# TODO: write tests in day08/test_weather_cli.py for format_forecast
