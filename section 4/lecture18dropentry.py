#How to drop the column and row in series,dataframe
import numpy as np
import pandas as pd

ser1=pd.Series(np.arange(3),index=['a','b','c'])
print(ser1)

print(ser1.drop('b'))

print("Dataframe drop column and series:")
df=pd.DataFrame(np.arange(9).reshape(3,3),index=['sy','nl','la'],columns=['pop','size','year'])
print(df)

print(df.drop('la'))
print(df.drop('year',axis=1))