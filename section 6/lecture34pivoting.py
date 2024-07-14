import pandas as pd
import numpy as np

def unpivot():
     data={'date':['2000-01-03','2000-01-04','2000-01-05','2000-01-03','2000-01-04','2000-01-05','2000-01-03','2000-01-04','2000-01-05'],
            'variable':['A','A','A','B','B','B','C','C','C'],
            'value':[-0.173441,0.206812,-0.95985,1.4193,0.9942,-0.8498,0.452197,-1.319614,-2.6039]}
     return pd.DataFrame(data,columns=['date','variable','value'])
df=unpivot()
print(df)

df_piv=pd.pivot_table(data=df,columns='date',aggfunc='mean')
print(df_piv)