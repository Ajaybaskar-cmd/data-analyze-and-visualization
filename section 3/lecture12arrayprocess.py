import numpy as np
import matplotlib.pyplot as plt
point=np.arange(-5,5,0.01)

dx,dy=np.meshgrid(point,point)
print(dx)

print(dy)

z=(np.sin(dx) + np.sin(dy))

print("--------------------------------")
print(z)
print("--------------------------------")
plt.imshow(z)
plt.show(block=True)