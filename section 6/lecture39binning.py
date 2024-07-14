import pandas as pd

year=[1990,1993,1994,1987,1998,2000,2001,2010,1987,1876,1910]
biiner=[1800,1900,2000,2010]
cat=pd.cut(year,biiner)
print(cat)