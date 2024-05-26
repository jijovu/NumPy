import numpy as np

arr=np.array([1,2,3,4,5])

x=arr.copy()
y=arr.view()
arr[4]=11
print(arr)
print(x)
print(y)
print(x.base)
print(y.base)