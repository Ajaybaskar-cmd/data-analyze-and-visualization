import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

df=pd.DataFrame(np.random.randn(1000,4))
print(df.head())

col=df[0]
print(col)

print(col[np.abs(col)>3])

print("dataframe")
z=np.abs(sc.stats.zscore(df[1]))
print(df[z>3])

plt.scatter(df[0],df[1])
plt.show(block=True)