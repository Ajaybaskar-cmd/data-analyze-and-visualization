import numpy as np
import pandas as pd
from pandas import Series,DataFrame

my_ser=Series([1,2,3,4],index=['a','b','c','d'])

print(my_ser)

print("Series indexes:")
my_ind=my_ser.index
print(my_ind)


print(my_ind[2])