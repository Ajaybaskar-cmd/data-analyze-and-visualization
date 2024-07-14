import pandas as pd
url='https://en.wikipedia.org/wiki/list_of_wealthiest_Americans_by_net_worth'

df=pd.read_html(url)
print(df)

df=df[0]

print("Correct dataframe")
print(df)

print(df.info())
df['Date of birth (age)'].str.replace(r'\{.*\}','',regex=True)

print(df.info())
print(df)

df['Date of birth (age)']=pd.to_datetime(df['Date of birth (age)'])



