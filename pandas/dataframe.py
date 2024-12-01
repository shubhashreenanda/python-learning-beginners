from operator import index

import pandas as pd
from idna.idnadata import scripts

from projectmanagement import Project

scores_dict = {'Kohili':[100,50,70],'Rohit':[100,88,0],
               'Surya':[20,4,77], 'Jadeja':[10,2,30]}

scores = pd.DataFrame(scores_dict)
scores.index = ['I1','I2','I3']
print(scores)

print('kohilis scrores')
print(scores.Kohili)

print(scores.loc['I1'])

print(scores.iloc[1])

print(scores.loc['I1':'I2'])
print(scores.iloc[0:2])

print(scores.loc[['I1','I3']])
print(scores.iloc[[0,1]])

print(scores.loc['I1':'I2',['Kohili','Surya']])
print(scores.iloc[[0,2],0:3])

print(scores[scores >= 90])
print(scores[(scores>=80) & (scores<=90)])

print(scores.at['I2','Kohili'])
print(scores.iat[2,0])
scores.at['I2','Kohili'] = 150
print(scores.at['I2','Kohili'])

scores.iat[2,0] = 200
print(scores.iat[2,0])

print(scores)
print(scores.mean())
print(scores.describe())
pd.set_option('display.precision',2)
print(scores.describe())
print(scores.T.describe())

print(scores.sort_index(ascending= False))
print(scores.sort_index(axis=1))
print(scores.sort_values(by='I1',axis=1,ascending=False))