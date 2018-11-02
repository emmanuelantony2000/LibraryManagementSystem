import variables
import pandas as pd
import numpy as np

#data = pd.DataFrame([['init', 'init', 'init', 1]], columns = variables.columns)
data = pd.DataFrame([['test', 'test', 'test', 1]], columns = variables.columns)
print(data)
#data.to_csv('books.csv')
data.to_pickle('books.pickle')
