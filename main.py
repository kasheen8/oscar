# -*- coding: utf-8 -*-

import parser
import bd



def main():
    complete_line = parser.xstavka_pars(parser.base_url_1x,parser.headers)
    bd.read_db(complete_line)


if __name__ == '__main__':
    main()








