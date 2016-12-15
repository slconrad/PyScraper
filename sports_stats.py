''' Scraper for pulling stats from ESPN'''

from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.espn.com/nfl/team/stats/_/name/dal')
soup = BeautifulSoup(page.content, 'html.parser')
