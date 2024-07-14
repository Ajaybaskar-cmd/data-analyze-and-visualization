import pandas as pd
import numpy as np
import sys

dframe=pd.read_csv(r'F:\UDEMY\Learnig data analysis and visualization\section 5\readandwrite.csv')
print(dframe)

dframe=pd.read_table(r'F:\UDEMY\Learnig data analysis and visualization\section 5\readandwrite.csv',header=None)

print(dframe)

print("HEADER")
df=pd.read_csv(r'F:\UDEMY\Learnig data analysis and visualization\section 5\readandwrite.csv',header=None)
#df.to_csv('E:\New folder\read.csv')
print(df)

df.to_csv(sys.stdout)

df.to_csv('E:\\New folder\\read.csv')