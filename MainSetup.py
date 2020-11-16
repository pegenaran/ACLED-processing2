import pandas as pd
import datetime as dt
import numpy as np
import csv
import os
import importlib
import RaptVectUtils
import event_utils
from collections import Counter
from RaptVectUtils import *
from event_utils import *
from mainglobals import *

def initialize_vars():
    df = pd.read_csv(main_db_file)
    countrylist = df.country.tolist()
    countrylist = list(set(countrylist))
    countrylist.sort()
    return df, countrylist

def make_country_codes():
    pass

def make_cmap(countrylist):
    clist = countrylist.copy()
    ctlist = []
    for c in clist:
        c = c.replace(' ','')
        c = c.replace(',','')
        c = c.replace('.','')
        ctlist.append(c[:12])
    # determined that at a string length of 12, all country names will still be unique
    # ctlist = [c[:12] for c in clist]
    cmap = {countrylist[i]: ctlist[i] for i in range(len(countrylist))}
    return cmap

def setup_countrydb(df, countrylist):
    cf_directory, cf_name, cfocus = find_country_directory(countrylist)
    cdb = df.loc[df.country == cfocus]
    return cdb, cf_directory, cf_name

def find_country_directory(countrylist):
    cmap = make_cmap(countrylist)
    print()
    print_multcols_list(countrylist, 4, 38)
    _, c_index = Get_int_ch("Choose a number of a country to setup the database: ", list(range(len(countrylist))), listisnums=True)
    c_index -= 1
    cf_directory = cmap[countrylist[c_index]] + '/'
    cf_name = cmap[countrylist[c_index]] + '_Current.csv'
    print('Expected directory: ', cf_directory)
    print('Expected filename: ', cf_name)
    return cf_directory, cf_name, countrylist[c_index]

def setup_country_directory(df, countrylist):
    runloop = True
    while runloop:
        cdb, cf_directory, cf_name = setup_countrydb(df, countrylist)
        if not os.path.exists(cf_directory):
            os.mkdir(cf_directory)
        cdb.to_csv(cf_directory + cf_name, index=False)
        runloop = 'y' == Get_str_ch_loc('','\nChoose another country? (y/n) ', ['y','n'])



if __name__ == "__main__":
    df, countrylist = initialize_vars()
    setup_country_directory(df, countrylist)


