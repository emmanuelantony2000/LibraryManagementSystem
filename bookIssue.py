from scanner import enter
import pandas as pd
import numpy as np
import datetime
import variables

gap = 13

data = pd.read_pickle('issue.pickle')
print(data)

newline = enter()

condition = not (data[data[variable.issue[0]] == newline[0]]).empty
now = pd.Timestamp((datetime.datetime.now()).strftime('%Y-%m-%d'))

if condition:
    diff = data.loc[(data[variables.input[0]]==newline[0]) & \
    (data[variables.input[1]]==newline[1]) & \
    (data[variables.input[2]]==newline[2]) & \
    (data[variables.input[2]]==newline[2]), variables.input[-1]] - now
    print(diff)
else:
    newline.append(now)
    newline.append(now+timedelta(13))
    newline = pd.DataFrame([newline], columns=variables.issue)
    data = data.append(newline, ignore_index=True)
