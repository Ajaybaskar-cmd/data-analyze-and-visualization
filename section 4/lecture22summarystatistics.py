import numpy as np
import pandas as pd

arr=np.array([[1,2,np.nan],[np.nan,3,4]])
df=pd.DataFrame(arr,index=['A','B'],columns=['one','two','three'])

print(df)
print("SUM of columns")
print(df.sum())
print('sum of row')
print(df.sum(axis=1))

print("Minimum value:")
print(df.min())

print('minimum index')
print(df.idxmin())