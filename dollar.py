import requests
import datetime
import re
from bs4 import BeautifulSoup
from os import system

 
dollor_var = ''
url = 'http://www.tgju.org/dollar-chart'
session = requests.session()
while True :
    site = session.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    for sitedata in soup.find_all('td', class_='nf'):
        dollor_money = dollor_var
        if dollor_money != sitedata.string :
            print("تغییر قیمت")
            print(datetime.datetime.now().time())
            print(sitedata.string)
            system('cvlc win.wanv')
            


        dollor_var = sitedata.string
        break
