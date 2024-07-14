import pandas as pd
import numpy as np

df=pd.DataFrame({'city':['thiruvarur','tanjavur','thiruchi'],
                'people':[2000,3000,4000]})
print(df)

df['head']=df['city'].map({'thiruvarur':'engan','tanjavur':'kumbakonam','thiruchi':'manaparai'})
print(df)