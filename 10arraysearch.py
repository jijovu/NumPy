import numpy as np

arr1 =np.array([7,1,2,3,4,5,6])
arr2 =np.array([[1,2,3],[4,5,6],[7,8,9]])


five = np.where(arr1 == 5)
even = np.where(arr1%2 ==0)
odd = np.where(arr2%2 ==1)
sort =np.searchsorted(arr1,7)
mul_sort =np.searchsorted(arr1,[7,8])

print(five)
print("index of even numbers :\n",even)
print("index of odd numbers :\n",odd)
print("sorting index :\n",sort)
print("multiple sorting index :\n",mul_sort)


