import pandas as pd
import numpy as np

df=pd.DataFrame(np.arange(16).reshape(4,4))
print(df)

blender=np.random.permutation(4)
print(blender)

taker=df.take(blender)
print(taker)

bos=np.array([1,2,3])
print(bos)
shaker=np.random.randint(0,len(bos),size=10)

print(shaker)

hand=bos.take(shaker)
print(hand)