import numpy as np
import pandas as pd
from pandas import DataFrame,Series

arr=np.arange(9).reshape(3,3)
print(arr)

#concatenate array
print(np.concatenate([arr,arr],axis=1))

#concatenate series
ser1=Series([1,2,3],index=['T','U','V'])
ser2=Series([4,5],index=['X','Y'])
print(ser1)
print(ser2)

print(pd.concat([ser1,ser2]))
print(pd.concat([ser1,ser2],axis=1))
print(pd.concat([ser1,ser2],axis=0,keys=['cat1','cat2']))

#concatenate dataframes
df1=DataFrame(np.random.randn(4,3),columns=['X','Y','Z'])
df2=DataFrame(np.random.randn(3,3),columns=['Y','Q','X'])
print(df1)
print(df2)

print("Concatenate dataframes")
print(pd.concat([df1,df2],ignore_index=True))
df1