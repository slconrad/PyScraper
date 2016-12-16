''' Scraper for pulling stats from ESPN'''

from bs4 import BeautifulSoup
import requests
import csv

page = requests.get('http://www.espn.com/nfl/team/stats/_/name/dal')
soup = BeautifulSoup(page.content, 'html.parser')

# Find the team
team_name = soup.find(class_='logo').get_text()
team_stats = soup.find(class_='sub-title').get_text()
team_leaders = soup.find(class_='mod-container mod-stat-leaders')

# Find the players
players = [p.get_text() for p in soup.select(".player-info")]

# Write to CSV
# TODO 'http://stackoverflow.com/questions/4607920/python-strip-html-from-text-data'
with open('sports_stats.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([team_name, team_stats, team_leaders])


print('\n')
print(team_name + ', ' + team_stats)
print('====================')
print(players)
print('Written to file.')
