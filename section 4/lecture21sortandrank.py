import numpy as np
import pandas as pd

ser1=pd.Series([1,2,3,4],index=['c','a','b','d'])
print(ser1)

print(ser1.sort_index())

ser2=pd.Series(np.random.randn(10))
print(ser2)

print(ser2.sort_values())


print(ser2.rank())