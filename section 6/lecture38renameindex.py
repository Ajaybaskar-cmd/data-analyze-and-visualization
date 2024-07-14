import numpy as np
import pandas as pd

df=pd.DataFrame(np.arange(12).reshape(3,4),index=['ny','la','sf'],
                columns=['a','b','c','d'])
print(df)
print(df.rename(index=str.upper))
print(df.rename(index={'ny':'ajay'},columns={'a':'ajay'}))
print(df.replace(1,np.nan))