import pandas as pd
import numpy as np
from scanner import scan
import variables
import sys

l = sys.argv
del l[0]
l = ''.join(l)
l = l.split('separator')

if len(l) == 3:
    # data = pd.read_csv('books.csv')
    data = pd.read_pickle('books.pickle')
    print(data)
    # data.dropna(inplace = True)
    # newline = scan()
    newline = l

    print(data[variables.input[0]], newline)

    # condition = (data[variables.input[0]] == newline[0])[0]
    # condition = not (data[data[variables.input[0]] == newline[0]]).empty

    condition = True
    for i in range(len(newline)):
        temp = not (data[data[variables.input[i]] == newline[i]]).empty
        condition = condition and temp

    print(condition)
    print(data[variables.input[0]])
    print(variables.input[0])
    print(newline[0])

    if condition:
        data.loc[(data[variables.input[0]]==newline[0]) & \
        (data[variables.input[1]]==newline[1]) & \
        (data[variables.input[2]]==newline[2]), variables.input[-1]] += 1
    else:
        newline.append(1)
        print(newline)
        newline = pd.DataFrame([newline], columns=variables.input)
        data = data.append(newline, ignore_index=True)

    # data = data.union(newline)
    # data.to_csv('books.csv')
    data.to_pickle('books.pickle')

    import shutil
    shutil.copy('books.pickle', 'books1.pickle')

    data = pd.read_pickle('books1.pickle')
    data.to_excel('books1.xlsx')

    print('Done')
