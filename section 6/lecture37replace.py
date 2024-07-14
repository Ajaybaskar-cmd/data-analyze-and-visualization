import pandas as pd
import numpy as np

ser=pd.Series([1,2,3,4,1,2,3,4])
print(ser)

print(ser.replace(1,np.nan))
print(ser.replace([1,2],[100,200]))
 
