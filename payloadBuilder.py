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

def getCategories(soup):
    categories = soup.find('div', class_='info').find('h4').text.strip()
    return categories

def getDetails(user_url):
    url = base_site_url+user_url
    soup = souper(url=url)
    detailsDictionary = getCategories(soup)
    
    # gets name value
    name = soup.find('div', class_="coach-name clearfix").find('span').text
    # gets address value
    address = getAddress(soup)
    # gets  phone value
    phone = getNum(soup)
    # gets categories value
    categories = getCategories(soup)

    detailsDictionary = {
        'name' : name,
        'address' : address,
        'phone' : phone,
        'categories' : categories
    }

    newDict = genderHourlyRate(soup)

    detailsDictionary.update(newDict)
    return detailsDictionary


details1 = getDetails("/users/john-bulman")



print(details1)
