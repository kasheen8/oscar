# -*- coding: utf-8 -*-

import pandas as pd
import sqlite3
import time
from oscar_db import complete_line

model_line_1x = complete_line


def full_analysis(model_line): #функция для просмотра полной таблицы изменений коэффициентов с временем по каждой номинации
    con = sqlite3.connect('oscar.sqllite3')
    full_df = pd.read_sql("SELECT * from coef", con, index_col = 'id')
    for line in model_line:
        for nomination in line:
            print(nomination)
            for nominee in line[nomination]:
                print(nominee)
                coef_list = full_df[(full_df.coef_label == nominee) & (full_df.nom_id == model_line.index(line) + 1)]['coef'].unique()
                for coef in coef_list:
                    print(coef,time.ctime(int(full_df[(full_df.coef == coef)]['timestamp'].head(1))), '-' * 30, sep = '\n')
            print('\n\n\n')
    con.close()


def choice_nomination():
    pass

def main():
    full_analysis(model_line_1x)


if __name__ == '__main__':
    main()