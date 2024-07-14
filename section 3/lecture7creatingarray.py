import numpy as np 

#creating array
my_list1=[1,2,3,4]
my_array1=np.array(my_list1)
print(my_array1)

print(type(my_array1))
print(my_array1.dtype)

#two dimensional array
my_list2=[11,22,33,44]
my_list=[my_list1,my_list2]
my_array2=np.array(my_list)
print("Two dimensional array:")
print(my_array2)

print(my_array2.shape)

empty=np.empty(5)
print(empty)

print(np.eye(2))

print(np.arange(5))
print(np.arange(5,40,4))

print(np.ones(5))
print(my_array2.ndim)
mylist=[my_list1,my_list2,[111,222,333,444]]
arr=np.array(mylist)
print(arr)

print(arr.ndim)

#three dimension array
value=[[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]
value_arr=np.array(value)
print(value_arr)
print(value_arr.ndim)
print(value_arr.shape )