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
    request = session.post(base_url, headers=headers, params = {'ids' : 5325}) #делаем запрос на ajax
    if request.status_code == 200:
        full_request = json.loads(request.text)
        print(full_request)
        print(full_request['reply']['sports']['38']['chmps']['5325']['evts'].keys())
        print(full_request['reply']['sports']['38']['chmps']['5325']['evts'])
        titles = []
        coefficients = []
        for iter in list(full_request['reply']['sports']['38']['chmps']['5325']['evts'].keys()):
            titles.append(full_request['reply']['sports']['38']['chmps']['5325']['evts'][iter]['name_ht'])
            coefficients.append(full_request['reply']['sports']['38']['chmps']['5325']['evts'][iter]['main']['69']['data'][iter]['blocks']['YNm']['Y']['kf'])
        nomin_title = full_request['reply']['sports']['38']['chmps']['5325']['name_ch']
        print(nomin_title)
        print(titles)
        print(coefficients)
        my_dict = {titles[i]: coefficients[i] for i in range(len(titles))}
        print(my_dict)
    else:
        print('ERROR')

def main():
    betcity_pars(base_url,headers)

if __name__ == '__main__':
    main()