''' Scraper for pulling stats from ESPN and logging to CSV'''

from bs4 import BeautifulSoup
import requests
import csv


page = requests.get('http://www.espn.com/nfl/team/stats/_/name/dal')
soup = BeautifulSoup(page.content, 'html.parser')

# Find the team
team_name = soup.find(class_='logo').get_text()
team_stats = soup.find(class_='sub-title').get_text()

# Find the players
team_leaders = [p.get_text(" ", strip=True)
                for p in soup.select(".mod-container .mod-stat")]

# Write to CSV
with open('sports_stats.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([team_name, team_stats, team_leaders])

print('\n')
print(team_name + ', ' + team_stats)
print('====================')
print(team_leaders)
print('====================')
print('Written to file.')
