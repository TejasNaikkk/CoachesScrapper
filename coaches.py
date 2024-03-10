import requests
from bs4 import BeautifulSoup

import config

base_url = config.url

page = 1

url = f'{base_url}+{page}'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')



print(soup.title.text)