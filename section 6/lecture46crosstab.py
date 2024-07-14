import pandas as pd

data={'sample':[1,2,3,4,5,6],
      'Animal':['dog','dog','cat','cat','dog','cat'],
      'intelligence':['smart','smart','dump','dump','dump','smart']}

df=pd.DataFrame(data)
print(df)

print(pd.crosstab(df.Animal,df.intelligence,margins=True))