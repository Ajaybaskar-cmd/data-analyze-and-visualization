import pandas as pd
from pandas import read_html
import numpy as np
url='https://www.fdic.gov/bankindividual/failed/banklist.html'

dframe_list=pd.io.html.read_html(url)
df=dframe_list[0]
print(df)