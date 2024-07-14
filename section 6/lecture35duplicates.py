import pandas as pd
import numpy as np

data={'key1':['a','a','b','b','b'],
      'key2':[2,2,3,3,3]}

df=pd.DataFrame(data)
print(df)

print(df.duplicated())

print(df.drop_duplicates())