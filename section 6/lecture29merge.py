import pandas as pd
import numpy as np

df1=pd.DataFrame({'key':['X','Y','Z','Z','X','X'],'data_set_1':np.arange(6)})
print(df1)

df2=pd.DataFrame({'key':['Q','Y','Z'],'data_set_2':[1,2,3]})
print(df2)

print(pd.merge(df1,df2))

print(pd.merge(df1,df2,on='key'))

print(pd.merge(df1,df2,on='key',how='left'))

print(pd.merge(df1,df2,on='key',how='right'))

print(pd.merge(df1,df2,on='key',how='outer'))

print(pd.merge(df1,df2,on='key',how='inner'))


df3=pd.DataFrame({'key':['X','X','X','Y','Z','Z'],'data_set_3':range(6)})
df4=pd.DataFrame({'key':['Y','Y','X','X','Z'],'data_set_4':range(5)})
print(df3)

print(df4)


print(pd.merge(df3,df4))

df_left=pd.DataFrame({'key':['sf','sf','la'],
                      'key2':['one','two','one'],
                      'data_left':[10,20,30]})

df_right=pd.DataFrame({'key':['sf','sf','la','la'],
                       'key2':['one','one','two','two'],
                       "data_right":[40,50,60,70]})

print(df_left)
print(df_right)

print(pd.merge(df_left,df_right,on=['key','key2'],how='outer'))

print(pd.merge(df_left,df_right,on='key'))


print(pd.merge(df_left,df_right,on='key',suffixes=('_lefty','_righty')))