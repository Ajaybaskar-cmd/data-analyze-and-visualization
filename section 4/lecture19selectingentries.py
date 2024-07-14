import numpy as np
import pandas as pd

ser=pd.Series(np.arange(3),index=['a','b','c'])

print(ser)

print(ser['c'])
print(ser.iloc[1])

print("VALUES RANGE")
print(ser<2)


print("Data Frame:")
dframe=pd.DataFrame(np.arange(25).reshape(5,5),index=['nyc','lc','ky','na','kd'],columns=['a','b','c','d','e'])

print(dframe)

print(dframe[['b','c']])

print(dframe<10)
print(dframe.loc['kd'])