from scanner import enter
import pandas as pd
import numpy as np
import datetime
import variables
import sys

l = sys.argv
del l[0]
l = ''.join(l)
l = l.split('separator')

gap = 13

if len(l) == 4:
    data = pd.read_pickle('issue.pickle')
    print(data)

    # newline = enter()
    newline = l

    cond = not data[(data[variables.issue[0]]==newline[0]) & \
    (data[variables.issue[1]]==newline[1]) & \
    (data[variables.issue[2]]==newline[2]) & \
    (data[variables.issue[3]]==newline[3])].empty

    books = pd.read_pickle('books.pickle')
    if (not (books[(books[variables.input[2]] == newline[3])&\
    (books[variables.input[3]] != 0)]).empty) or cond:
        condition = not (data[(data[variables.issue[0]]==newline[0]) & \
        (data[variables.issue[1]]==newline[1]) & \
        (data[variables.issue[2]]==newline[2]) & \
        (data[variables.issue[3]]==newline[3])]).empty
        now = pd.Timestamp((datetime.datetime.now()).strftime('%Y-%m-%d'))
        print(variables.issue[-1])
        if condition:
            print(data.loc[(data[variables.issue[0]]==newline[0]) & \
            (data[variables.issue[1]]==newline[1]) & \
            (data[variables.issue[2]]==newline[2]) & \
            (data[variables.issue[3]]==newline[3]), \
            variables.issue[-1]]-now)
            print(now)

            diff = (data.loc[(data[variables.issue[0]]==newline[0]) & \
            (data[variables.issue[1]]==newline[1]) & \
            (data[variables.issue[2]]==newline[2]) & \
            (data[variables.issue[3]]==newline[3]), \
            variables.issue[-1]] - now)
            # print(diff.values[0])
            diff = (diff.astype('timedelta64[D]').astype(int)).values[0]
            # diff.astype(pd.Timedelta).apply(lambda l: l.days)

            
            # diff = (data.loc[(data[variables.input[0]]==newline[0]) & \
            # (data[variables.input[1]]==newline[1]) & \
            # (data[variables.input[2]]==newline[2]), variables.input[-1]] - now).days
            
            # print(diff, type(diff), diff.values[0])
            print(diff)
            if diff < 0:
                diff = -diff
                fine = (2**(diff//7)-1)*7 + (diff%7)*(2**(diff//7))
                print(fine)
                array = [newline[0], newline[1], newline[3], fine, \
                now-datetime.timedelta(gap+diff), now]
                array = pd.DataFrame([array], columns=variables.fine)
                f = pd.read_pickle('fine.pickle')
                f = data.append(array, ignore_index=True)
                f.to_pickle('fine.pickle')
                f.to_excel('fine.xlsx')
            data = data.drop(data[(data[variables.issue[0]]==newline[0]) & \
            (data[variables.issue[1]]==newline[1]) & \
            (data[variables.issue[2]]==newline[2]) & \
            (data[variables.issue[3]]==newline[3])].index)
            data.to_pickle('issue.pickle')
            data.to_excel('issue.xlsx')
            data = pd.read_pickle('issue1.pickle')
            data.loc[(data[variables.issue[0]]==newline[0]) & \
            (data[variables.issue[1]]==newline[1]) & \
            (data[variables.issue[2]]==newline[2]) & \
            (data[variables.issue[3]]==newline[3]), \
            variables.issue[-1]] = now
            data.to_pickle('issue1.pickle')
            data.to_excel('issue1.xlsx')
            books.loc[books[variables.input[2]]==newline[3], variables.input\
            [-1]] += 1
        else:
            books.loc[books[variables.input[2]]==newline[3], variables.input\
            [-1]] -= 1
            newline.append(now)
            newline.append(now+datetime.timedelta(gap))
            newline.append(now+datetime.timedelta(gap))
            newline = pd.DataFrame([newline], columns=variables.issue)
            data = data.append(newline, ignore_index=True)
            data.to_pickle('issue.pickle')
            data.to_excel('issue.xlsx')
            data = pd.read_pickle('issue1.pickle')
            data = data.append(newline, ignore_index=True)
            data.to_pickle('issue1.pickle')
            data.to_excel('issue1.xlsx')
    books.to_pickle('books.pickle')
