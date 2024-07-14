import numpy as np
import pandas as pd
df_left=pd.DataFrame({'key':['X','Y','Z','X','Y'],
                      'data':range(5)})
print(df_left)

df_right=pd.DataFrame({'group_data':[10,20]},index=['X','Y'])
print(df_right)

print(pd.merge(df_left,df_right,right_on='group_data',left_index=True))

print(df_left.join(df_right))

left_df=pd.DataFrame({'key':['sf','sf','sf','la','la'],
                      'key2':[10,20,30,20,30],
                      'data':range(5)})
print(left_df)

right_df=pd.DataFrame(np.arange(10).reshape(5,2),index=[['la','la','sf','sf','sf'],[10,20,20,10,10]],
                      columns=['col1','col2'])
print(right_df)

print(pd.merge(left_df,right_df,left_on=['key','key2'],right_index=True))

print(left_df.join(right_df))