import variables
import pandas as pd

#data = pd.DataFrame([['init', 'init', 'init', 1]], columns = variables.columns)
data = pd.DataFrame(columns = variables.columns)
print(data)
#data.to_csv('books.csv')
data.to_pickle('books.pickle')
