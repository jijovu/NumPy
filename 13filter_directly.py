import numpy as np

arr =np.array([1,11,22,2,33,3])

filter_arr = arr>3

newarr =arr[filter_arr]
print("newarr :\n",newarr)

even =arr%2==0

even_arr = arr[even]

print("even_arr :\n",even_arr)