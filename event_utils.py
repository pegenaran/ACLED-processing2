import pandas as pd
import datetime as dt

def Get_a_date(inputstr):
    dateloop = True
    while dateloop:
        datestr = input(inputstr)
        if datestr == '':
            print('Invalid entry. Please try again.')
        else:
            if datestr != 'n':
                try:
                    dateval = pd.Timestamp(datestr).date()
                    dateloop = False
                except ValueError:
                    print('Incorrect format. Try again.')
            else:
                dateval = dt.datetime.now().date()
                dateloop = False
    return datestr, dateval

def make_strlist(list1):
    return [str(x) for x in list1]

def make_truncstrlist(list1, truncval):
    return [str(x)[:truncval] for x in list1]

# sort and remove duplicates from a list
def sort_rmv_dupl(list1):
    list1 = make_strlist(list1)
    list1 = list(set(list1))
    list1.sort()
    return list1