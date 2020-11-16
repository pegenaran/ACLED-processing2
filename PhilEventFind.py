import pandas as pd
import datetime as dt
import numpy as np
import csv
import importlib
import RaptVectUtils
importlib.reload(RaptVectUtils)
import phil_globalvars
importlib.reload(phil_globalvars)
import event_utils
importlib.reload(event_utils)
from RaptVectUtils import *
from phil_globalvars import *
from event_utils import *

df = pd.read_csv(phildata_stem + "Philippines_Current.csv")

# df
# df.event_date[len(df)-1:]
cols = df.columns.tolist()
locations = sort_rmv_dupl(df.location.tolist())
event_types = sort_rmv_dupl(df.event_type.tolist())
sub_event_types = sort_rmv_dupl(df.sub_event_type.tolist())
admin1_list = sort_rmv_dupl(df.admin1.tolist())
admin2_list = sort_rmv_dupl(df.admin2.tolist())
admin3_list = sort_rmv_dupl(df.admin3.tolist())

# admin1 is the list of regions
# admin2 is the list of provinces
# admin3 is the list of cities and/or municipalities
# admin4 is the list of baranggays
# then lat and long give the precise location
# the database can be segregated according to these geographical delineations

# print_multcols_list(cols, 4, numexpand=30, include_idx=True)
# print()
# print_multcols_list(event_types, 2, numexpand=55)
# print()
# print_multcols_list(admin2_list, 3, numexpand=30)
# print()
# print_multcols_list(admin3_list, 3, numexpand=35)
# print()
# df[['inter2','event_date','event_type','year','timestamp','admin1']].tail()

def initialize_event_df(main_df):
    event_df = main_df.copy()
    event_df = main_df[colstouse].copy()
    event_df.event_date = pd.to_datetime(event_df.event_date, format='%d %B %Y').dt.date
    event_df.set_index('event_date', inplace=True)
    event_df.sort_index(inplace=True)
    event_df['Reg_code'] = event_df.admin1
    event_df.Reg_code.replace(regnames_map2, inplace=True)
    event_df['Region'] = np.where(
        ((event_df.Reg_code == 'BARMM') | (event_df.Reg_code == 'CAR') | (event_df.Reg_code == 'NCR')),
        event_df.Reg_code,
        event_df.admin1)
    actor1_complist = make_truncstrlist(event_df.actor1, 20)
    assoc_actor1_complist = make_truncstrlist(event_df.assoc_actor_1, 20)
    actor2_complist = make_truncstrlist(event_df.actor2, 20)
    assoc_actor2_complist = make_truncstrlist(event_df.assoc_actor_2, 20)    
    event_df['comp_act1'] = actor1_complist
    event_df['comp_assoc_act1'] = assoc_actor1_complist
    event_df['comp_act2'] = actor2_complist
    event_df['comp_assoc_act2'] = assoc_actor2_complist
    event_df.rename(columns={'admin2':'Province',
          'admin3':'Municipality',
          'location':'Baranggay'}, inplace=True)
    
    return event_df[cols_order]

def get_months():
    date_df = pd.read_csv(phildata_stem + 'dateseg.csv')
    date_df.startdate = pd.to_datetime(date_df.startdate, format="%Y-%m-%d").dt.date
    date_df.enddate = pd.to_datetime(date_df.enddate, format="%Y-%m-%d").dt.date
    date_df.set_index('startdate', inplace=True)
    return date_df

def make_monthly_divs(main_df):
    today = dt.datetime.now().date()
    event_df = initialize_event_df(main_df)
    date_df = get_months()
    
    for sd in date_df.index.tolist():
        if sd <= today:
            enddate = date_df.loc[sd, 'enddate']
            mmonth_df = event_df.loc[sd:enddate]
            fnamestr = str(sd.year) + '_' + "{0:0=2d}".format(sd.month) + '_PhilEvents.csv'
#             print(fnamestr)
            mmonth_df[cols_order].to_csv(phildata_stem + fnamestr, quoting=csv.QUOTE_ALL)
#     return(mmonth_df[cols_order])

make_monthly_divs(df)
    
def filter_event_choices(event_df):
    cols = event_df.columns.tolist()
    print_multcols_list(cols, 4, numexpand=30, include_idx=True, use_limit=True)
    print()
    _, colnum = Get_int_ch('Enter the number of the column to filter on: ', 
                   list(range(1, len(cols)+1)), listisnums=True, allowenter=False)
    colhdr = cols[colnum-1]
    coltype_list = event_df[colhdr].tolist()
    coltype_list = sort_rmv_dupl(coltype_list)
    coltype_strlist = make_strlist(coltype_list)
    coltype_strlist.sort()
    print()
    print_multcols_list(coltype_strlist, 2, numexpand=55, include_idx=True, use_limit=True)
    print()
    _, coltypenum = Get_int_ch('Enter the number of the item to filter on: ', 
                   list(range(1, len(coltype_list)+1)), listisnums=True, allowenter=False)
    coltype = coltype_list[coltypenum-1]
    
    return colhdr, coltype

def num_events_bydate(main_df):
    event_df = initialize_event_df(main_df)
    date_df = get_months()
    colhdr, coltype = filter_event_choices(event_df)
    
    _, filtdate = Get_a_date("Enter year and month to view in YYYY-MM format, or 'n' to go back: ")
    print(filtdate)
    enddate = date_df.loc[filtdate, 'enddate']
    mmonth_df = event_df.loc[filtdate:enddate]
    print(coltype)
    mmonth_df = mmonth_df.loc[mmonth_df[colhdr] == coltype]
    print('For the month and year of: ', filtdate)
    print('There were ' + str(len(mmonth_df)) + ' incidents in the category: ' + coltype.upper())
    return mmonth_df

def choose_multfilt(event_df):
    _, filtnum = Get_int_ch('Enter the number of the filters up to 4: ', 
        list(range(1,5)), listisnums=True, allowenter=False)
    
    colfiltlist = []
    for f in range(filtnum):
        colhdr, coltype = filter_event_choices(event_df)
        colfiltlist.append([colhdr, coltype])
    return colfiltlist, filtnum
    
def filter_single_month(mmonth_df, colfiltlist, filtnum):
    for f in range(filtnum):
        if colfiltlist[f][0] == 'fatalities':
            # look for the filter number greater than or equal to the number of fatalities on the filter
            mmonth_df[colfiltlist[f][0]] = mmonth_df[colfiltlist[f][0]].astype(int)
            mmonth_df = mmonth_df.loc[mmonth_df[colfiltlist[f][0]] >= int(colfiltlist[f][1])]
        else:
            mmonth_df = mmonth_df.loc[mmonth_df[colfiltlist[f][0]] == colfiltlist[f][1]]
    return mmonth_df

def mult4_filt(main_df):
    event_df = initialize_event_df(main_df)
    date_df = get_months()
    colfiltlist, filtnum = choose_multfilt(event_df)
    
    # choose other columns to display in the summary
    cols = event_df.columns.tolist()
    print_multcols_list(cols, 4, numexpand=30, include_idx=True, use_limit=True)
    print('\nChoose 1 more column to include in the summary display.')
    _, colnum = Get_int_ch('Enter the number of the column to include: ', 
                   list(range(1, len(cols)+1)), listisnums=True, allowenter=False)
    dispcol1 = cols[colnum-1]
    dispcol2 = 'Num_events'
        
    _, begdate = Get_a_date("\nEnter year and month of beginning month of the study in YYYY-MM format: ")
    _, findate = Get_a_date("Enter year and month of final month in YYYY-MM format: ")
    
    datelist = date_df.loc[begdate:findate].index.tolist()
    rowlist = []
    seg_participants = []
    for d in datelist:
        enddate = date_df.loc[d, 'enddate']
        mmonth_df = event_df.loc[d:enddate]
        mmonth_df = filter_single_month(mmonth_df, colfiltlist, filtnum)
        segregate_list = mmonth_df[dispcol1].tolist()
        segregate_list = list(set(segregate_list))
        numevents = len(mmonth_df)
        seg_parts = len(segregate_list)
        # print(mmonth_df)
        # print(segregate_list)
        rowlist.append([d.strftime("%b-%Y"), seg_parts, numevents])
        seg_participants = seg_participants + segregate_list
        
    # print(rowlist)
    # print(['Num_of ' + dispcol1, 'Num_events_tot'])
    summary_df = pd.DataFrame(rowlist, columns=['Month','Num_of ' + dispcol1, 'Num_events_tot'])
    summary_df.set_index('Month', inplace=True)
    summary_df = summary_df.loc[summary_df['Num_events_tot'] !=0]
    seg_participants = list(set(seg_participants))
    seg_participants.sort()
    
    print('\nThe following summary used these filters: ')
    for f in range(filtnum):
        print('Filter ' + str(f+1) + ': ' + colfiltlist[f][0] + ': ' + colfiltlist[f][1])
    print()
    print(summary_df)
    print('\nThese are the variety of hits over the entire period for the Number of ' + dispcol1 + ':')
    print_multcols_list(seg_participants, 3, numexpand=35, use_limit=True)

def view_single_month_filt(main_df):
    pd.set_option("display.max_colwidth", 35)
    event_df = initialize_event_df(main_df)
    cols = event_df.columns.tolist()
    date_df = get_months()
    colfiltlist, filtnum = choose_multfilt(event_df)
    
    colhdr_list = []
    print_multcols_list(cols, 4, numexpand=30, include_idx=True, use_limit=True)
    _, numcols = Get_int_ch('Enter the number of columns to include in the display: ', 
                    list(range(1, len(cols)+1)), listisnums=True, allowenter=False)
    for c in list(range(1, numcols+1)):
        _, colnum = Get_int_ch('Enter the index number for column ' + str(c) + ': ', 
                    list(range(1, len(cols)+1)), listisnums=True, allowenter=False)
        colhdr_list.append(cols[colnum-1])
    
    _, modate = Get_a_date("\nEnter year and month of the data you want to view in YYYY-MM format: ")

    enddate = date_df.loc[modate, 'enddate']
    mmonth_df = event_df.loc[modate:enddate]
    mmonth_df = filter_single_month(mmonth_df, colfiltlist, filtnum)

    # set the record numbers in order to choose to display
    mmonth_df.reset_index(inplace=True)
    colhdr_list = ['event_date'] + colhdr_list
    mmonth_df.index = mmonth_df.index + 1
    # mmonth_df.set_index('index', inplace=True)
    
    repeatloop = True
    while repeatloop:
        print(mmonth_df[colhdr_list])
        repeatloop = 'y' == Get_str_ch_loc('','Print the list again? (y/n) ', ['y','n'])
    detailch = 'y' == Get_str_ch_loc('','View details of one record? (y/n) ', ['y','n'])
    while detailch:
        _, recnum = Get_int_ch('Choose the record number to view: ', 
                    list(range(1, len(mmonth_df)+1)), listisnums=True, allowenter=False)
        disp_df = mmonth_df[recnum-1:recnum] #[colhdr_list]
        print(disp_df.iloc[0])
        lastcol = disp_df.columns.tolist()[len(disp_df.columns.tolist())-1]
        sources = disp_df['source'].iloc[0] 
        print('\nSources: ', sources)
        notes = disp_df['notes'].iloc[0]
        print('Notes: ', notes)
        detailch = 'y' == Get_str_ch_loc('','\nView another record? (y/n) ', ['y','n'])
        if detailch:
            print()
            print(mmonth_df[colhdr_list])

    return mmonth_df[colhdr_list]

def main_menu_items():
    mystr_list = []
    mystr_list.append('\nChoose from the following options: ')
    mystr_list.append('\n1 - Filter the events and view by month ')
    mystr_list.append('\n2 - View details of a single month ')
    mystr_list.append('\n3 - Exit program ')
    return mystr_list

if __name__ == "__main__":
    mystr_list = main_menu_items()
    menustr = ''
    for s in mystr_list:
        menustr = menustr + s
    while True:
        print()
        menuch = Get_str_ch_loc(menustr,'Pick a number: ', list_to_strlist(list(range(len(mystr_list)))))
        if menuch == '1':
            mult4_filt(df)
        elif menuch == '2':
            view_single_month_filt(df)
        elif menuch == '3':
            exit()