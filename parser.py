# -*- coding: utf-8 -*-

import urllib.request #библиотека для работы с сетью
import requests
from bs4 import BeautifulSoup as bs #библиотека для парсинга html
import lxml

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
           }

base_url = 'https://betcity.ru/ru/line/culture/5325'

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def betcity_pars(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print(request.content)
        soup = bs(request.content,'lxml')
        # div = soup.find_all('div',atrrs={'class':'container'})
        print(soup)
        # print('-' * 200)
        # print(soup2)
    else:
        print('ERROR')

def main():
    betcity_pars(base_url,headers)

if __name__ == '__main__':
    main()