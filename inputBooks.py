import pandas as pd
import numpy as np
from scanner import scan
import variables

#data = pd.read_csv('books.csv')
data = pd.read_pickle('books.pickle')
print(data)
#data.dropna(inplace = True)
newline = scan()
print(data[variables.columns[0]], newline)

#condition = (data[variables.columns[0]] == newline[0])[0]
condition = not (data[data[variables.columns[0]] == newline[0]]).empty
print(condition)
print(data[variables.columns[0]])
print(variables.columns[0])
print(newline[0])

if condition:
    data.loc[data[variables.columns[0]]==newline[0], \
    variables.columns[-1]] += 1
else:
    newline.append(1)
    print(newline)
    new = pd.DataFrame([newline], columns=variables.columns)
    data = data.append(new, ignore_index=True)

#data = data.union(newline)
#data.to_csv('books.csv')
data.to_pickle('books.pickle')

import shutil
shutil.copy('books.pickle', 'Books.pickle')

data = pd.read_pickle('Books.pickle')
data.to_excel('Books.xlsx')

print('Done')
