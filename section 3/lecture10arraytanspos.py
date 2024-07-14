import numpy as np
arr=np.arange(50).reshape((10,5))
print(arr)

print(arr.T)

arr1=np.array(([1,2],[3,4]))
arr2=np.array(([1,2],[3,4]))
print(arr1)
arr_mul=np.dot(arr1,arr2)
print("Multiply of the array arr1,arr2:")
print(arr_mul)

print(np.dot(arr.T,arr))

arr3d=np.arange(50).reshape((5,5,2))
print(arr3d)

arr=np.array(([1,2,3]))
print(arr)

print(arr.swapaxes(0,1))