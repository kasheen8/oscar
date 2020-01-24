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
base_url_1x = 'https://1xstavka.ru/LineFeed/GetGameZip?id=%s&lng=ru&cfview=0&isSubGames=true&GroupEvents=true&allEventsGroupSubGames=true&countevents=250&partner=51&grMode=2' #URL XHR запроса



def betcity_pars(base_url, headers):                                                #парсинг коэффициентов с betcity
    ids_betcity = [5325, 5326, 5327, 5328, 5329, 5330, 5331, 7902, 7903, 25370]
    full_pars = []
    for ids in ids_betcity:
        session = requests.Session() #создаем сессию
        request = session.post(base_url, headers=headers, params = {'ids' : ids}) #делаем запрос на ajax
        if request.status_code == 200:
            full_request = json.loads(request.text)
            titles = []
            coefficients = []
            for iter in list(full_request['reply']['sports']['38']['chmps'][str(ids)]['evts'].keys()):
                titles.append(full_request['reply']['sports']['38']['chmps'][str(ids)]['evts'][iter]['name_ht'])
                coefficients.append(full_request['reply']['sports']['38']['chmps'][str(ids)]['evts'][iter]['main']['69']['data'][iter]['blocks']['YNm']['Y']['kf'])
            nomin_title = full_request['reply']['sports']['38']['chmps'][str(ids)]['name_ch']
            print(nomin_title)
            full_line = {titles[i]: coefficients[i] for i in range(len(titles))}
            print(full_line)
            full_line = {nomin_title : full_line}
            full_pars.append(full_line)
        else:
            print('ERROR')
    return full_pars


def xstavka_pars(base_url, headers):                                            #парсинг коэффицентов с 1xbet
    ids_1x = [41193103, 66779703, 67495559, 67500025, 67500027, 67500021, 67727525, 67727527, 67368117, 67381125,
              66776853, 66777749, 66777739, 66776927, 66776851, 67379461, 67380037, 67380035, 67381769, 67371115,
              67371117, 67377887, 67378015, 67379459]
    full_pars = []
    for ids in ids_1x:
        line_url = base_url % ids
        session = requests.Session()  # создаем сессию
        request = session.get(line_url, headers=headers, params={'ids': ids})  # делаем запрос на ajax
        if request.status_code == 200:
            full_request = json.loads(request.text)
            full_line = full_request['Value']['GE'][0]['E'][0]
            name_line = full_request['Value']['O1']
            print(name_line)
            line = []
            for iter in full_line:
                line.append({iter['PL']['N']:iter['C']})
            print(line)
            complete_line = {name_line : line}
            full_pars.append(complete_line)
        else:
            print('ERROR')
    return full_pars


def main():
    print(betcity_pars(base_url_betcity_xhr,headers))
    print(xstavka_pars(base_url_1x,headers))


if __name__ == '__main__':
    main()