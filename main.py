import requests
from bs4 import BeautifulSoup
from souper import souper
from payloadBuilder import getDetails
import config

base_url = config.url


page = 1
url = f'{base_url}{page}'
soup = souper(url)
# section = soup.find('section', class_='directory').find_all('div', class_= 'avatar')
# users = []
# for div in section:
#     As = div.find_all('a')
#     for a in As:
#         href = a['href']
#         # print(href)
#         users.append(href)
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

print(len(users))

# print(div.text.strip())



# for user in users:
#     details1 = getDetails(user)
#     print(details1)
