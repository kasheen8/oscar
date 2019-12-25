# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs #библиотека для парсинга html
import lxml
import json

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
           }

base_url = 'https://ad.betcity.ru/d/off/events?rev=6&ver=48&csn=ooca9s' #URL XHR запроса


def betcity_pars(base_url, headers):
    session = requests.Session() #создаем сессию
    request = session.post(base_url, headers=headers, params = {'ids' : 5326}) #делаем запрос на ajax
    if request.status_code == 200:
        print(json.loads(request.text))
    else:
        print('ERROR')

def main():
    betcity_pars(base_url,headers)

if __name__ == '__main__':
    main()