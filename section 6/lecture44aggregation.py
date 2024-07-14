import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r'F:\\csv file\winequality-red.csv',sep=';')
print(df.head())

print(df.agg('mean'))

def maxtomin(arr):
    return arr.max()-arr.min()

wino=df.groupby('quality')
print(wino.mean())

print(wino.agg(maxtomin))

print(df.pivot_table(index=['quality']))

plt.scatter(x=df['quality'],y=df['alcohol'])
plt.show(block=True)