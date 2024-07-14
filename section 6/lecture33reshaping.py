import numpy as np
import pandas as pd

df=pd.DataFrame(np.arange(8).reshape(2,4),
                index=pd.Index(['sf','la'],name='city'),
                columns=pd.Index(['a','b','c','d'],name='letter'))
print(df)
df_set=df.stack()
print(df_set)

print(df_set.unstack())
print(df_set.unstack('city'))

ser1=pd.Series([1,2,3],index=['x','y','z'])
ser2=pd.Series([4,5,6],index=['q','x','y'])

dframe=pd.concat([ser1,ser2],keys=['alpha','beta'])
print(dframe)

print(dframe.unstack())