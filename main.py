import requests
from bs4 import BeautifulSoup
from souper import souper
import config

base_url = config.url

links = []
for i in range(1,10):
    page = i
    url = f'{base_url}{page}'
    links.append(url)
