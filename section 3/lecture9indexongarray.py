import numpy as np
arr=np.arange(0,11)
print(arr)

print(arr[0])

print(arr[0:5])
arr[0:4]=100
print(arr)

arr=np.arange(0,11)
print(arr)

slice_arr=arr[0:5]
print(slice_arr)

slice_arr[:]=99
print(slice_arr)
print(arr)

arr_copy=arr.copy()
print(arr_copy)


#two dimensional

arr_2d=np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)

print("0-row:",arr_2d[0])

print("0,1 value of two dimensional array:",arr_2d[0][1])

print("slicing:")
print(arr_2d[0:2,0:3])


print("Zeros array:")
arr2d=np.zeros([5,5])
print(arr2d)

#fancy indexing\
arr_l=arr2d.shape[1]
print(arr_l)
for i in range(arr_l):
    arr2d[i]=i
    
print(arr2d)