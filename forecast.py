""" Web scraper utilizing BeautifulSoup and Pandas """

from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get(
    "http://forecast.weather.gov/MapClick.php?lat=33.1276&lon=-96.8737")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[1]

period = tonight.find(class_="period-name").get_text(" ")
short_desc = tonight.find(class_="short-desc").get_text(" ")
temp = tonight.find(class_="temp").get_text()

img = tonight.find("img")
desc = img['title']
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods
short_descs = [sd.get_text()
               for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img\n")]

# ['Tonight',
#  'Thursday',
#  'ThursdayNight',
#  'Friday',
#  'FridayNight',
#  'Saturday',
#  'SaturdayNight',
#  'Sunday',
#  'SundayNight']

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_desc,
    "temp": temps,
    "desc": descs
})

weather

print(period)
print(temp)
print(short_desc)
print("=============")
print(descs)
# print('=============')
# print(short_descs)
# print(temps)
# print(descs)
# print('=============')
