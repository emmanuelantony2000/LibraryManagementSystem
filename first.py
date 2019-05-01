from datetime import timedelta
import variables
import pandas as pd
import numpy as np

#data = pd.DataFrame([['init', 'init', 'init', 1]], columns = variables.input)
data = pd.DataFrame([['test', 'test', 'test', 1]], columns = variables.input)
print(data)
#data.to_csv('books.csv')
data.to_pickle('books.pickle')
data = pd.DataFrame([['test', 'test', 'test', 'test', \
pd.Timestamp('2000-01-01'), pd.Timestamp('2000-01-01')+timedelta(5), \
pd.Timestamp('2000-01-01')+timedelta(6)]], columns = variables.issue)
#data = pd.DataFrame([['test', 'test', 'test', pd.Timestamp(2000, 00, 00), \
#pd.Timestamp(2000, 00, 00)]], columns = variables.issue)
print(data)
data.to_pickle('issue.pickle')

data = pd.DataFrame([['data', 'data', 'data', 0, pd.Timestamp('2000-01-01'), \
pd.Timestamp('2000-01-01')+timedelta(5)]], columns = variables.fine)
print(data)
data.to_pickle('fine.pickle')

import shutil
shutil.copy('issue.pickle', 'issue1.pickle')
