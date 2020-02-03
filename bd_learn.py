# -*- coding: utf-8 -*-

import time
import sqlite3


def sqlite3_simple_example_create_db():
    con = sqlite3.connect('base.db')

    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS core_fes(Well TEXT,'
                                                    'Sample TEXT,'
                                                    'Porosity FLOAT,'
                                                    'Swr FLOAT,'
                                                    'Permeability FLOAT)')

    cur.execute('INSERT INTO core_fes VALUES("Yellow snake creek", "Sample #666", 25.6, 34, 16)')
    data = ["Green snake creek", "Sample #111", 24, 20, 34]
    cur.execute('INSERT INTO core_fes VALUES(?, ?, ?, ?, ?)', data)
    big_data = []
    data1 = ["Brown snake creek", "Sample #333", 15, 2, 33]
    data2 = ["Dark snake creek", "Sample #222", 20, 17, 55]
    big_data.append(data1)
    big_data.append(data2)

    for data_unit in big_data:
        cur.execute('INSERT INTO core_fes VALUES(?, ?, ?, ?, ?)', data_unit)

    con.commit()
    cur.close()
    con.close()

def print_data_2d(columns_names, data):
    print(columns_names)
    for line in data:
        print(line)
    print('number of lines in database table is '+str(len(data)))






def sqlite_simple_read_db(data_base, table, column_name = None):
    con = sqlite3.connect(data_base)
    cur = con.cursor()
    query_columns = 'pragma table_info('+table+')'
    cur.execute(query_columns)
    columns_description = cur.fetchall()
    columns_names = []
    for column in columns_description:
        columns_names.append(column[1])

    if column_name is None:
        query = 'SELECT * FROM '+table
        cur.execute(query)
        data = cur.fetchall()
    else:
        query = 'SELECT '+column_name+' FROM '+table
        cur.execute(query)
        data = cur.fetchall()
        new_data = []
        for element in data:
            new_data.append(element[0])
        data = new_data
        del(new_data)
    print_data_2d(columns_names, data)
    cur.close()
    con.close()

def sqlite3_simple_delete_table(data_base, table):
    con = sqlite3.connect(data_base)
    cur = con.cursor()
    query = 'DROP TABLE IF EXISTS '+table
    cur.execute(query)
    cur.close()
    con.close()

def sqlite3_simple_delete_record(data_base, table, id_column, id_record):
    con = sqlite3.connect(data_base)
    cur = con.cursor()

    query = 'DELETE FROM '+table+' WHERE '+id_column+" = '"+id_record+"'"
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()

def sqlite3_simple_update_record(data_base, table, id_column, id_record, param_column, param_val):
    con = sqlite3.connect(data_base)
    cur = con.cursor()

    query = 'UPDATE '+table+' SET '+param_column+'='+str(param_val)+' WHERE '+id_column+" = '"+str(id_record)+"'"
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()

def main():
    data_base = 'base.db'
    table = 'core_fes'
    id_column = 'Sample'
    id_record = 'Sample #333'
    param_column = 'Porosity'
    param_val = 9
    #sqlite3_simple_example_create_db()
    #sqlite3_simple_delete_table(data_base,table)
    #sqlite3_simple_delete_record(data_base,table,id_column,id_record)
    sqlite3_simple_update_record(data_base, table, id_column, id_record, param_column, param_val)
    sqlite_simple_read_db(data_base, table)


if __name__ == '__main__':
    main()