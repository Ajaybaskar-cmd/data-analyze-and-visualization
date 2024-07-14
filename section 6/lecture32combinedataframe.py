import numpy as np
import pandas as pd

ser1=pd.Series([1,np.nan,3,np.nan],index=['q','r','s','t'])
ser2=pd.Series(np.arange(len(ser1)),dtype=np.int64,index=['q','r','s','t'])
print(ser1)
print(ser2)

print(pd.Series(np.where(pd.isnull(ser1),ser2,ser1),index=ser1.index))

print(ser1.combine_first(ser2))
n=np.nan
df_odds=pd.DataFrame({'X':[1,n,3,n],
                      'Y':[5,n,7,n],
                      'Z':[9,n,11,n]})
print(df_odds)

print(df_odds.dtypes)

df_evens=pd.DataFrame({'X':[2,n,4,6,8,10],
                       'Y':[12,14,16,n,18,20]})
print(df_evens)

print(df_odds.combine_first(df_evens))

df=pd.DataFrame({'X':[1,2,3,4],
                 'y':[1,2,3,n]})
print(df.dtypes)

df['X']=df['X'].astype(float)
print(df.dtypes)