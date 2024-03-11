import requests
from bs4 import BeautifulSoup
from souper import souper
import config

base_site_url = config.base_site_url

def getAddress(soup):
    # Getting Address
    address_img = soup.find('img', alt='Location: ')
    if address_img:
        address_li = address_img.find_parent('li')
        if address_li:
            address = address_li.get_text(strip=True)
    return address

def getNum(soup):
    phone_img=soup.find('img', alt = 'Phone')
    if phone_img:
        phone_li = phone_img.find_parent('li')
        if phone_li:
            phone = phone_li.get_text(strip=True)
    return phone

def genderHourlyRate(soup):
    li_tags = soup.find_all('li')

    # Dictionary to return gender and hourly rate
    ghr = {}
    # Loop through <li> tags to find gender and hourly rate
    for li in li_tags:
        text = li.get_text(strip=True)
        if text.startswith('Gender'):
            gender = text.split(':')[-1].strip()
            g = {
                'gender' : gender
            }
            ghr.update(g)
        if text.startswith('Hourly Rate'):
            hourly_rate = text.split(':')[-1].strip()
            hr = {
                'Hourly Rate' : hourly_rate
            }
            hr.update(hr)
            ghr.update(hr)
    return ghr


def getDetails(user_url):
    url = base_site_url+user_url
    soup = souper(url=url)
    name = soup.find('div', class_="coach-name clearfix").find('span').text

    # calling getAddress function
    address = getAddress(soup)
    #calling getNum function
    phone = getNum(soup)

    detailsDictionary = {
        'name' : name,
        'address' : address,
        'phone' : phone
    }

    newDict = genderHourlyRate(soup)

    detailsDictionary.update(newDict)
    return detailsDictionary


details1 = getDetails("/users/marla-williams")

details2 = getDetails("/users/liz-wolfe")

print(details1)
print(details2)