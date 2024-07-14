import pandas as pd
import numpy as np

data={'Flavour':['max chocolate chip','chocolate','vanila','cookie dough','rocky road','pistachio','cake butter',
                 'naopoltan','choclate fodge brownie'],
      'Base flavour':['vanila','chocolate','vanila','vanila','chocolate','vanila','vanila',
                      'vanila','chocolate'],
      'Liked':['yes','yes','no','yes','yes','no','yes','no','yes'],
      'Flavour rating':[10.0,8.8,4.7,6.9,8.2,2.3,6.5,3.8,8.2],
      'Texture rating':[8,7.6,5,6.5,7,3.4,6,5,7],
      'Total rating':[18,16,9.7,13.4,15.2,5.7,12.5,8.8,15.3]}
df=pd.DataFrame(data)
print(df)

dframe=pd.DataFrame({'k1':['X','X','Y','Y','Z'],
                     'k2':['alpha','beta','alpha','beta','alpha'],
                     'dataset1':np.random.randn(5),
                     'dataset2':np.random.randn(5)})
print(dframe)

group=dframe['dataset1'].groupby(dframe['k1'])
print(group.mean())

cities=['NA','LA','LA','NA','NA']
month=['jan','feb','jan','feb','jan']

print(dframe['dataset1'].groupby([cities,month]).mean())


print(dframe.groupby('k1').max())

#for loop condition for seperating
for name,group in dframe.groupby('k1'):
    print("this is the %s group"%name)
    print(group)
    print('\n')
    
for (k1,k2),group in dframe.groupby(['k1','k2']):
    print("key1=%s key2=%s"%(k1,k2))
    print(group)
    print('\n')

#change for dictionary values
d=dict(list(dframe.groupby('k1')))
print(d['X'])