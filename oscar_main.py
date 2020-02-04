# -*- coding: utf-8 -*-

import oscar_parser as ospa
import oscar_db as osdb
import time


def add_data_30min():
    while True:
        complete_line = ospa.xstavka_pars(ospa.base_url_1x,ospa.headers)
        osdb.read_db(complete_line)
        time.sleep(1800)
def main():
    add_data_30min()


if __name__ == '__main__':
    main()








