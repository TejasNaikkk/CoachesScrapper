import requests
from bs4 import BeautifulSoup
from souper import souper
import config

base_url = config.url


page = 1
url = f'{base_url}{page}'
soup = souper(url)
section = soup.find('section', class_='directory').find_all('div', class_= 'avatar')
a = []
for div in section:
    As = div.find_all('a')
    for a in As:
        href = a['href']
        print(href)
# div = section.find_all('div', class_ = 'coach')
# print(div)
# for a_tag in a_tags:
#     href_value = a_tag['href']
#     print(href_value)


