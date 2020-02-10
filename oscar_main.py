# -*- coding: utf-8 -*-

import oscar_parser as ospa
import oscar_db as osdb
import oscar_dataanalysis as osdataan
import time


def add_data_1hour(): #запись коэффициентов в бд каждый час
    while True:
        print(time.ctime(time.time()))
        complete_line = ospa.xstavka_pars(ospa.base_url_1x,ospa.headers)
        osdb.read_db(complete_line)
        print('-' * 100)
        time.sleep(3600)

def main():
    add_data_1hour()
    osdataan.full_analysis(osdataan.model_line_1x)

if __name__ == '__main__':
    main()








