
# converts a list to one single long string
def list_to_str_nospace(list1):
    newstr = ''
    list1.sort()
    for i in list1:
        newstr = newstr + str(i)
    return newstr

# converts a list to an identical length list, with all entries converted to strings
def list_to_strlist(list1):
    newlist = []
    for i in list1:
        newlist.append(str(i))
    return newlist

# prints multiple columns of any list, from 2 to 5 columns
# this does not print a dataframe
def print_multcols_list(list1,numcols,numexpand=35,include_idx=True, use_limit=False):
    if use_limit:
        expandval = numexpand - 8
    else:
        expandval = numexpand
    if numcols in [2,3,4,5,6,7,8,9]:
        # num_oncol = int(len(list1) / numcols)   # the number of entries to be listed in a single column
        loopnumend = int(len(list1) / numcols)
        extraloop = len(list1) % numcols
        
        # still need to modify this loop so that the tab delimitation is set for 2, 4, or 5 columns also
        if include_idx:
            print('There are ',len(list1),' entries in the list.')
        for x in list(range(0,loopnumend)):
            if numcols == 2:
                if include_idx:
                    mystr = (str(x+1) + ": " + list1[x][:expandval] + 
                        '\t' + str(x+loopnumend+1) + ": " + list1[x + loopnumend][:expandval])
                else:
                    mystr = (list1[x] + 
                        '\t' + list1[x + loopnumend])
                print(mystr.expandtabs(numexpand))
                # print(list1[x],list1[x + loopnumend])
            elif numcols == 3:
                if include_idx:
                    mystr = (str(x+1) + ": " + list1[x][:expandval] + 
                        '\t' + str(x+loopnumend+1) + ": " + list1[x + loopnumend][:expandval] + 
                        '\t' + str(x+loopnumend*2+1) + ": " + list1[x + loopnumend*2][:expandval])
                else:
                    mystr = (list1[x] + 
                        '\t' + list1[x + loopnumend][:expandval] + 
                        '\t' + list1[x + loopnumend*2][:expandval])
                print(mystr.expandtabs(numexpand))
            elif numcols == 4:
                if include_idx:
                    mystr = (str(x+1) + ": " + list1[x][:expandval] + 
                        '\t' + str(x+loopnumend+1) + ": " + list1[x + loopnumend][:expandval] + 
                        '\t' + str(x+loopnumend*2+1) + ": " + list1[x + loopnumend*2][:expandval] + 
                        '\t' + str(x+loopnumend*3+1) + ": " + list1[x + loopnumend*3][:expandval])
                else:
                    mystr = (list1[x][:expandval] + 
                        '\t' + list1[x + loopnumend][:expandval] + 
                        '\t' + list1[x + loopnumend*2][:expandval] + 
                        '\t' + list1[x + loopnumend*3][:expandval])
                print(mystr.expandtabs(numexpand))
            elif numcols == 5: 
                if include_idx:
                    mystr = (str(x+1) + ": " + list1[x][:expandval] + 
                        '\t' + str(x+loopnumend+1) + ": " + list1[x + loopnumend][:expandval] + 
                        '\t' + str(x+loopnumend*2+1) + ": " + list1[x + loopnumend*2][:expandval] + 
                        '\t' + str(x+loopnumend*3+1) + ": " + list1[x + loopnumend*3][:expandval] + 
                        '\t' + str(x+loopnumend*4+1) + ": " + list1[x + loopnumend*4][:expandval])
                else:
                    mystr = (list1[x][:expandval] + 
                        '\t' + list1[x + loopnumend][:expandval] + 
                        '\t' + list1[x + loopnumend*2][:expandval] + 
                        '\t' + list1[x + loopnumend*3][:expandval] + 
                        '\t' + list1[x + loopnumend*4][:expandval])
                print(mystr.expandtabs(numexpand))
            elif numcols == 6: 
                if include_idx:
                    mystr = (str(x+1) + ": " + list1[x][:expandval] + 
                        '\t' + str(x+loopnumend+1) + ": " + list1[x + loopnumend][:expandval] + 
                        '\t' + str(x+loopnumend*2+1) + ": " + list1[x + loopnumend*2][:expandval] + 
                        '\t' + str(x+loopnumend*3+1) + ": " + list1[x + loopnumend*3][:expandval] + 
                        '\t' + str(x+loopnumend*4+1) + ": " + list1[x + loopnumend*4][:expandval] +
                        '\t' + str(x+loopnumend*5+1) + ": " + list1[x + loopnumend*5][:expandval])
                else:
                    mystr = (list1[x][:expandval] + 
                        '\t' + list1[x + loopnumend][:expandval] + 
                        '\t' + list1[x + loopnumend*2][:expandval] + 
                        '\t' + list1[x + loopnumend*3][:expandval] + 
                        '\t' + list1[x + loopnumend*4][:expandval] +
                        '\t' + list1[x + loopnumend*5][:expandval])
                print(mystr.expandtabs(numexpand))
            elif numcols == 7: 
                if include_idx:
                    mystr = (str(x+1) + ": " + list1[x][:expandval] + 
                        '\t' + str(x+loopnumend+1) + ": " + list1[x + loopnumend][:expandval] + 
                        '\t' + str(x+loopnumend*2+1) + ": " + list1[x + loopnumend*2][:expandval] + 
                        '\t' + str(x+loopnumend*3+1) + ": " + list1[x + loopnumend*3][:expandval] + 
                        '\t' + str(x+loopnumend*4+1) + ": " + list1[x + loopnumend*4][:expandval] +
                        '\t' + str(x+loopnumend*5+1) + ": " + list1[x + loopnumend*5][:expandval] +
                        '\t' + str(x+loopnumend*6+1) + ": " + list1[x + loopnumend*6][:expandval])
                else:
                    mystr = (list1[x][:expandval] + 
                        '\t' + list1[x + loopnumend][:expandval] + 
                        '\t' + list1[x + loopnumend*2][:expandval] + 
                        '\t' + list1[x + loopnumend*3][:expandval] + 
                        '\t' + list1[x + loopnumend*4][:expandval] +
                        '\t' + list1[x + loopnumend*5][:expandval] +
                        '\t' + list1[x + loopnumend*6][:expandval])
                print(mystr.expandtabs(numexpand))
            elif numcols == 8:
                if include_idx:
                    mystr = (str(x+1) + ": " + list1[x][:expandval] + 
                        '\t' + str(x+loopnumend+1) + ": " + list1[x + loopnumend][:expandval] + 
                        '\t' + str(x+loopnumend*2+1) + ": " + list1[x + loopnumend*2][:expandval] + 
                        '\t' + str(x+loopnumend*3+1) + ": " + list1[x + loopnumend*3][:expandval] + 
                        '\t' + str(x+loopnumend*4+1) + ": " + list1[x + loopnumend*4][:expandval] +
                        '\t' + str(x+loopnumend*5+1) + ": " + list1[x + loopnumend*5][:expandval] +
                        '\t' + str(x+loopnumend*6+1) + ": " + list1[x + loopnumend*6][:expandval] +
                        '\t' + str(x+loopnumend*7+1) + ": " + list1[x + loopnumend*7][:expandval])
                else:
                    mystr = (list1[x][:expandval] + 
                        '\t' + list1[x + loopnumend][:expandval] + 
                        '\t' + list1[x + loopnumend*2][:expandval] + 
                        '\t' + list1[x + loopnumend*3][:expandval] + 
                        '\t' + list1[x + loopnumend*4][:expandval] +
                        '\t' + list1[x + loopnumend*5][:expandval] +
                        '\t' + list1[x + loopnumend*6][:expandval] +
                        '\t' + list1[x + loopnumend*7][:expandval])
                print(mystr.expandtabs(numexpand))
            else:       # implies number of columns is 9
                if include_idx:
                    mystr = (str(x+1) + ": " + list1[x][:expandval] + 
                        '\t' + str(x+loopnumend+1) + ": " + list1[x + loopnumend][:expandval] + 
                        '\t' + str(x+loopnumend*2+1) + ": " + list1[x + loopnumend*2][:expandval] + 
                        '\t' + str(x+loopnumend*3+1) + ": " + list1[x + loopnumend*3][:expandval] + 
                        '\t' + str(x+loopnumend*4+1) + ": " + list1[x + loopnumend*4][:expandval] +
                        '\t' + str(x+loopnumend*5+1) + ": " + list1[x + loopnumend*5][:expandval] +
                        '\t' + str(x+loopnumend*6+1) + ": " + list1[x + loopnumend*6][:expandval] +
                        '\t' + str(x+loopnumend*7+1) + ": " + list1[x + loopnumend*7][:expandval] +
                        '\t' + str(x+loopnumend*8+1) + ": " + list1[x + loopnumend*8][:expandval])
                else:
                    mystr = (list1[x][:expandval] + 
                        '\t' + list1[x + loopnumend][:expandval] + 
                        '\t' + list1[x + loopnumend*2][:expandval] + 
                        '\t' + list1[x + loopnumend*3][:expandval] + 
                        '\t' + list1[x + loopnumend*4][:expandval] +
                        '\t' + list1[x + loopnumend*5][:expandval] +
                        '\t' + list1[x + loopnumend*6][:expandval] +
                        '\t' + list1[x + loopnumend*7][:expandval] +
                        '\t' + list1[x + loopnumend*8][:expandval])
                print(mystr.expandtabs(numexpand))
        if extraloop !=0:
            mystr = ''
            for x in list(range(loopnumend * numcols,loopnumend * numcols + extraloop)):
                if include_idx:
                    mystr = mystr + str(x+1) + ": " + list1[x][:expandval] + '\t'
                else:
                    mystr = mystr + list1[x][:expandval] + '\t'
            print(mystr.expandtabs(numexpand))

    else:
        print('Must choose 2 to 9 columns. No output generated.')

    return len(list1)

def Get_str_ch_upc(headerstr, strinput, list_of_strs):
    loop1 = True
    while loop1:
        if headerstr != '':
            print(headerstr)
        enterstr = input(strinput)
        enterstr = enterstr.upper()
        if enterstr in list_of_strs:
            loop1 = False
        else:
            print('Invalid entry. Please try again.')
    return enterstr

def Get_str_ch_loc(headerstr, strinput, list_of_strs):
    loop1 = True
    while loop1:
        if headerstr != 'nodown':
            print(headerstr)
        enterstr = input(strinput)
        enterstr = enterstr.lower()
        if enterstr in list_of_strs:
            loop1 = False
        else:
            print('Invalid entry. Please try again.')
    return enterstr

def Get_int_ch(strinput, intlist, listisnums=False, allowenter=False):
    if listisnums:
        newlist = []
        for s in intlist:
            newlist.append(str(s))
        intlist = newlist
    loop1 = True
    while loop1:
        enterstr = input(strinput)
        if allowenter and enterstr == '':
            return enterstr, 0
        if enterstr in intlist:
            loop1 = False
            newint = int(enterstr)
        else:
            print('Invalid entry. Please try again.')
    return enterstr, newint

def check_dict(dict1):
    try:
        list1 = dict1[0]
    except KeyError:
        print('KeyError - dictionary value returned: ', dict1)
        list1 = []
    return list1