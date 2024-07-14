import pandas as pd

data=pd.ExcelFile('F:\csv file\housing.xlsx')
df=data.parse('Sheet1')

df.fillna(0)
df.to_csv('F:\\csv file\\housingdataforcleaning.csv')