import numpy as np
import pandas as pd

ser=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(ser)

ser2=ser.reindex(['a','b','c','d','e','f'])
print(ser2)


ser3=ser.reindex(['a','b','c','d','e','f','g'],fill_value=0)
print(ser3)

#method using value of fill the series
s=pd.Series(['usa','mexico','canada'])
print(s)

rg=list(range(15))
print(rg)

s1=s.reindex(rg,method='ffill')
print(s1)

#redindex using dataframe
df=pd.DataFrame(np.random.randn(25).reshape(5,5),index=['A','B','C','D','E'],columns=['col1','col2','col3','col4','col5'])
print(df)

df2=df.reindex(['A','B','C','D','E','F'])

print(df2)


