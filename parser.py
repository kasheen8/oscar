# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs #библиотека для парсинга html
import lxml
import json

headers = {'accept': '*/*',
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
           }
#headers = {'accept': '*/*',
#           'user-agent': 'Chrome/78.0.3904.108'}

base_url_betcity_xhr = 'https://ad.betcity.ru/d/off/events?rev=6&ver=48&csn=ooca9s' #URL XHR запроса
base_url_1x = 'https://1xstavka.ru/line/TV-Games/1871418-Academy-Awards-2020-Special-bets/41193103-Academy-Awards-2020-Best-Picture-Winner/' #URL
ids_betcity = [5325, 5326, 5327, 5328,135354, 135355]


def betcity_pars(base_url, headers):
    session = requests.Session() #создаем сессию
    request = session.post(base_url, headers=headers, params = {'ids' : 5326}) #делаем запрос на ajax
    if request.status_code == 200:
        full_request = json.loads(request.text)
        print(full_request)
        print(full_request['reply']['sports']['38']['chmps']['5326']['evts'].keys())
        print(full_request['reply']['sports']['38']['chmps']['5326']['evts'])
        titles = []
        coefficients = []
        for iter in list(full_request['reply']['sports']['38']['chmps']['5326']['evts'].keys()):
            titles.append(full_request['reply']['sports']['38']['chmps']['5326']['evts'][iter]['name_ht'])
            coefficients.append(full_request['reply']['sports']['38']['chmps']['5326']['evts'][iter]['main']['69']['data'][iter]['blocks']['YNm']['Y']['kf'])
        nomin_title = full_request['reply']['sports']['38']['chmps']['5326']['name_ch']
        print(nomin_title)
        print(titles)
        print(coefficients)
        full_line = {titles[i]: coefficients[i] for i in range(len(titles))}
        print(full_line)
    else:
        print('ERROR')


def xstavka_pars(base_url, headers):
    session = requests.Session()  # создаем сессию
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('OK')
        soup = bs(request.content,'lxml')
        div = soup.find_all('div', attrs={'span': 'data-coef'})
        print(soup)
    else:
        print('ERROR')
def main():
    #betcity_pars(base_url_betcity_xhr,headers)
    xstavka_pars(base_url_1x,headers)


if __name__ == '__main__':
    main()