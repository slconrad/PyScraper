''' Trending athletes as per Google search trends '''
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://finance.yahoo.com/quote/CL=F?p=CL=F'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
# Add quotes below
oil_name = soup.find(class_="D(ib) Fz(18px)").get_text()
oil_futures = soup.find(class_="Fw(b) Fz(36px) Mb(-4px)").get_text()
banner_names = soup.find_all(class_="Fz(s) Ell Fw(b) C($actionBlue)")
banner_futures = soup.find_all(class_="Fz(s) Mt(4px) Mb(0px) Fw(b) D(ib)")

# TODO: Fix banner rotation
gold_name = banner_names[0].string
gold_futures = banner_futures[0].string


print(oil_name + ': ' + oil_futures)
print(gold_name + ': ' + gold_futures)
