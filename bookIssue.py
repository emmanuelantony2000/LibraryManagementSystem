from scanner import enter
import pandas as pd
import numpy as np
import datetime
import variables

gap = 13

data = pd.read_pickle('issue.pickle')
print(data)

newline = enter()

condition = not (data[data[variables.issue[0]] == newline[0]]).empty
now = pd.Timestamp((datetime.datetime.now()).strftime('%Y-%m-%d'))

if condition:
    diff = ((data.loc[(data[variables.issue[0]]==newline[0]) & \
    (data[variables.issue[1]]==newline[1]) & \
    (data[variables.issue[2]]==newline[2]) & \
    (data[variables.issue[3]]==newline[3]), \
    variables.issue[-1]])[0] - now).date
    print(diff)
else:
    newline.append(now)
    newline.append(now+datetime.timedelta(13))
    newline = pd.DataFrame([newline], columns=variables.issue)
    data = data.append(newline, ignore_index=True)

data.to_pickle('issue.pickle')
