import numpy as np

arr=np.array(['a','b','c','d'])
#defining data type 
arr1=np.array([1,22,333,4444],dtype='i4')
arr2=np.array([1.1,2.1,2.3])
newarr2=arr2.astype(int)

print("arr data type =",arr.dtype)
print("arr1 data type =",arr1.dtype)
print("arr2 data type =",arr2.dtype)
print("newarr2 data type =",newarr2.dtype)
