import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)
newarr=arr.reshape(6,2)
print("newarr shape (6,2) :\n",newarr)

newarr01=arr.reshape(2,3,2)
print("newarr01 shape \n",newarr01)
del arr

arr=np.array([1,2,3,4,5,6,7,8])

print("check base",arr.reshape(2,4).base)

newarr = arr.reshape(2,2,-1)
print(newarr)
newarr1=newarr.reshape(-1)
print("3-D array reshaped into 1-D array :\n",newarr1)