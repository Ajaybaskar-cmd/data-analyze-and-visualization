import numpy as np
import pandas as pd

ser=pd.Series(np.random.randn(6),index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])
print(ser)

print(ser.index)

df1=ser.unstack()
print(df1)

df2=pd.DataFrame(np.arange(16).reshape(4,4),index=[['a','a','b','b'],[1,2,1,2]],columns=[['ny','ny','la','sf'],['cold','hot','cold','hot']])
print(df2)

print(df2.index)

df2.index.names=['index1','index2']
print(df2)