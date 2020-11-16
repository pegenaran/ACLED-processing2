import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
from phil_globalvars import *

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

def regionscrape():
    url = "https://en.wikipedia.org/wiki/Regions_of_the_Philippines#List_of_regions"

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup.prettify()
    # myelems =  soup.findAll("span", {"class": "mw-headline"})

    # extract all the tables in the HTML 
    table = soup.find_all('table', {"class":"wikitable sortable toptextcells"})
    table_rows = table[0].find_all('tr')

    table_headers = table[0].find_all('th')
    hdrs = [i.text[:len(i.text)-1] for i in table_headers]
    colslist = hdrs[1:9]
    rowlist = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text[:len(i.text)-1] for i in td]
        # print(len(row),row)
        if len(row) == 8:
            pos1 = row[0].index('(')
            pos2 = row[0].index(')')
            # print(row[0], len(row[0]), pos1, pos2)
            shortname = row[0][pos1+1:pos2]
            # print(shortname)
        else:
            shortname = ''
        rowlist.append(row + [shortname])

    df = pd.DataFrame(rowlist, columns=colslist + ['shortname'])
    # print(colslist)

    df.to_csv(phildata_stem + 'RegionalTable_draft.csv')

    return df

def fix_regtable(df):
    regtable = df.copy()
    if 'Unnamed: 0' in regtable.columns.tolist():
        regtable.drop(columns='Unnamed: 0', inplace=True)
    
    ahdr = 'Area(km2)'
    alist = regtable[ahdr].tolist()
    blist = [a[:len(a)-12] for a in alist]
    blist = [float(a.replace(',','')) for a in blist]
    # print(blist)
    regtable[ahdr] = blist
    regtable[ahdr] = regtable[ahdr].astype(float)

    pophdr = 'Population(2020 estimate)'
    poplist = regtable[pophdr].tolist()
    popnumlist = []
    for p in poplist:
        pos1 = p.index('(')
        # pos2 = p.index(')')
        newstrval = p[:pos1]
        newnumval = float(newstrval.replace(',',''))
        popnumlist.append(newnumval)
    regtable[pophdr] = popnumlist

    denshdr = 'Density'
    denslist = regtable[denshdr].tolist()
    densnumlist = []
    for d in denslist:
        pos1 = d.index('/')
        # pos2 = p.index(')')
        newstrval = d[:pos1]
        newnumval = float(newstrval.replace(',',''))
        densnumlist.append(newnumval)
    regtable[denshdr] = densnumlist

    return regtable

def provincescrape():
    url = "https://en.wikipedia.org/wiki/Provinces_of_the_Philippines#List"

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup.prettify()
    # myelems =  soup.findAll("span", {"class": "mw-headline"})

    # extract all the tables in the HTML 
    table = soup.find_all('table', {"class":"wikitable sortable plainrowheaders toptextcells"})
    table_rows = table[0].find_all('tr')

    # table_headers = table[0].find_all('th')
    # hdrs = [i.text[:len(i.text)-1] for i in table_headers]
    # colslist = hdrs[1:13]

    colslist = ['Province', 'Capital','', 'Population', 'Area', 'Density', 'Founded', 'Island_group', 'Region', 'Mun_LGUs','City_LGUs','Brgy_LGUs']

    rowlist = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text[:len(i.text)-1] for i in td]
        rowlist.append(row)

    df = pd.DataFrame(rowlist, columns=colslist)
    # print(hdrs)

    df.to_csv(phildata_stem + 'ProvincialTable_draft.csv')

    return df

def fix_provtable(df):
    provtable = df.copy()
    if 'Unnamed: 0' in provtable.columns.tolist():
        provtable.drop(columns='Unnamed: 0', inplace=True)

    provtable = provtable[2:len(provtable)-2]

    for c in provtable.columns.tolist():
        provtable[c] = remove_notes(provtable[c].tolist())

    ahdr = 'Area'
    alist = provtable[ahdr].tolist()
    blist = [a[:a.index('\xa0')] for a in alist]
    blist = [float(a.replace(',','')) for a in blist]
    # print(blist)
    provtable[ahdr] = blist
    provtable[ahdr] = provtable[ahdr].astype(float)

    pophdr = 'Population'
    poplist = provtable[pophdr].tolist()
    popnumlist = [float(p.replace(',','')) for p in poplist]
    provtable[pophdr] = popnumlist

    denshdr = 'Density'
    denslist = provtable[denshdr].tolist()
    densnumlist = []
    for d in denslist:
        pos1 = d.index('/')
        # pos2 = p.index(')')
        newstrval = d[:pos1]
        newnumval = float(newstrval.replace(',',''))
        densnumlist.append(newnumval)
    provtable[denshdr] = densnumlist

    return provtable

def remove_notes(list1):
    newlist = []
    for x in list1:
        if '[' in x:
            pos1 = x.index('[')
            newlist.append(x[:pos1])
        else:
            newlist.append(x)
    return newlist