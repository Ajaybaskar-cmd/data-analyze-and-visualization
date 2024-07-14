import numpy as np
arr=np.arange(11)
print(arr)

print("Square root of array:")
print(np.sqrt(arr))

print("Exponential of the array:")
print(np.exp(arr))

exp=2**2
print(exp)

print("Generate the random number:")
a=np.random.randn(10)
print(a)

b=np.random.randn(10)
print(b)

print("Add the random number:")
print(np.add(a,b))

print("Maximum of the array:")
print(np.maximum(a,b))

x=np.arange(5)
x[2]=-1
y=np.arange(6,11)
print(x,y)

pos=np.positive(x,y)
print(pos)