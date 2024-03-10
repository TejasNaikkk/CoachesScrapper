import config
import requests
from bs4 import BeautifulSoup

def souper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup