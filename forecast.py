""" Web scraper for polling weather forecasts utilizing
BeautifulSoup and Pandas """

from bs4 import BeautifulSoup
import requests

# Setup and retrieve
page = requests.get(
    "http://forecast.weather.gov/MapClick.php?lat=33.1276&lon=-96.8737")
soup = BeautifulSoup(page.content, 'html.parser')

# Current temp and weather
current = soup.find(id="current_conditions-summary")
# current_weather = current.find(class_="myforecast-current").get_text()
current_temp = current.find(class_="myforecast-current-lrg").get_text()

# Extended forecast
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
today = forecast_items[0]
today_forecast = today.find(class_="short-desc").get_text(" ")

period = today.find(class_="period-name").get_text(" ")
short_desc = today.find(class_="short-desc").get_text(" ")

# today temp today_temp = today.find(class_="temp-low").get_text()

img = today.find("img")
desc = img['title']
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text()
               for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# Print to console
print('Currently in DFW:')
print(today_forecast)
print(' ' + current_temp)
print(' today ' + period + ', ' + short_desc)
print('--------------')
print(' ' + 'Extended Forecast:')
print(descs)
# print('=============')
# print(short_descs)
# print(temps)
# print(periods)
# print('=============')
