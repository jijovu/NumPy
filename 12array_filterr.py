import numpy as np

arr =np.array([1,11,22,2,33,3])

x =arr[[False,True,True,False,True,False]]
print("x :\n",x)

filter_arr=[]

for element in arr:
    if element > 3:
        filter_arr.append(True)
    else :
        filter_arr.append(False)

newarr=arr[filter_arr]
print("newarr :\n",newarr)

even =[]

for i in arr:
    if i %2==0:
        even.append(True)
    else:
        even.append(False)
even_arr = arr[even]

print("even_arr :\n",even_arr)


