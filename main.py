import requests
from bs4 import BeautifulSoup
from souper import souper
from payloadBuilder import getDetails
import config
from csvBuilder import makeCSV
base_url = config.url


page = 1
url = f'{base_url}{page}'
soup = souper(url)

divs = soup.find_all('div', class_='coach')

for div in divs[:]:
    recommendation = div.find('div', class_='alert alert-warning clearfix')
    if recommendation:
        divs.remove(div)
users = []
for div in divs:
    a = div.find('a')
    href = a['href']
    users.append(href)


for user in users:
    payload = getDetails(user)
    makeCSV(payload)
