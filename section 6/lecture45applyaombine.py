import pandas as pd
import numpy as np

df_wine=pd.read_csv(r'F:\\csv file\\winequality-red.csv',sep=';')
print(df_wine.head())

def ranker(df):
    df['alc_content_rank']=np.arange(len(df))+1
    return df

df_wine.sort_values(by='alcohol',ascending=False,inplace=True)
df_wine=df_wine.groupby(df_wine['quality']).apply(ranker)
print(df_wine.head())


num=df_wine['quality'].value_counts()
print(num)

df_wine[df_wine.alc_content_rank==1].head(len(num))
print(df_wine.head())

