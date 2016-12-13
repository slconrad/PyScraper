'''Pull data from Wunderground website utilizing BeautifulSou and urllib
 to scrape and parse out temps based on set criteria then save to CSV'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

# Iterate over months, days
for m in range(0, 13):  # Set months to query
    for d in range(1, 32):
        if (m == 2 and d > 28):  # Feb
            break
        elif (m in [4, 6, 9, 11] and d > 30):
            break
        timestamp = '2016-' + str(m) + '_' + str(d)
        print('Getting data for ' + timestamp)
        url = "https://www.wunderground.com/history/airport/KDFW/2016/" + \
            str(m) + "/" + str(d) + "/DailyHistory.html"
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        wx = soup.find_all(class_="wx-value")
        dayTemp = wx[2].string
        dayAverage = wx[3].string
        # Format month
        if len(str(m)) < 2:
            mStamp = '0' + str(m)
        else:
            mStamp = str(m)
        # Format day
        if len(str(d)) < 2:
            dStamp = '0' + str(d)
        else:
            dStamp = str(d)
        # Timestamp
        timestamp = '2016' + mStamp + dStamp
        # Write to CSV
        with open('temp_history.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([timestamp, dayTemp, dayAverage])

print('Data recieved')
