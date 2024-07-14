import pandas as pd
import numpy as np

animal=pd.DataFrame(np.arange(16).reshape(4,4),
                    index=['dog','cat','bird','mouse'],
                    columns=['W','X','Y','Z'])
print(animal)

behaviour={'W':'good','X':'bad','Y':'good','Z':'bad'}
animal_col=animal.groupby(behaviour,axis=1)
print(animal_col.mean())

ser=pd.Series(behaviour)
print(ser)

print(animal.groupby(ser,axis=1).mean())
