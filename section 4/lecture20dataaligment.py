import numpy as np
import pandas as pd

ser1=pd.Series(np.arange(3),index=list('abc'))
print(ser1)

ser2=pd.Series(np.arange(3,7),index=list('cdef'))
print(ser2)

print(ser1+ser2)

dframe=pd.DataFrame(np.arange(4).reshape)