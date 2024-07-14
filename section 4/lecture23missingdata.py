import pandas as pd
import numpy as np

data=pd.Series(['one','two',np.nan,'four'])
print(data)

#find the index of the null row
print(data.isnull())

#delete the null row
print(data.dropna())

df=pd.DataFrame([[1,2,3],[np.nan,5,6],[np.nan,np.nan,np.nan]])
print(df)

#delete the null value rows
print(df.dropna())

#delete the all row null values
print(df.dropna(how='all'))

dframe=pd.DataFrame([[1,2,3,np.nan],[4,5,np.nan,6],[7,np.nan,np.nan,np.nan]])
print(dframe)


print("thresh the values to null")
print(dframe.dropna(thresh=1))

print("Fill the values in null value = 1")
print(dframe.fillna(1))


