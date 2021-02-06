import requests
import re
from bs4 import BeautifulSoup


def main():
     url = 'http://www.tgju.org/dollar-chart'
     session = requests.session()
     site = session.get(url)
     soup = BeautifulSoup(site.text, 'html.parser')
     price = soup.find('td', class_='nf')
     print("Price per dollar in Rials:", price.string)

main()
