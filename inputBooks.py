import pandas as pd
import numpy as np
from scanner import scan
import variables

#data = pd.read_csv('books.csv')
data = pd.read_pickle('books.pickle')
print(data)
data.dropna(inplace = True)
newline = scan()


newline = pd.DataFrame(scan(), columns=variables.columns)
data = data.append(newline, ignore_index=True)
#data = data.union(newline)
#data.to_csv('books.csv')
data.to_pickle('books.pickle')

import shutil
shutil.copy('books.pickle', 'Books.pickle')

print('Done')
