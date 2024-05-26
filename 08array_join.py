import numpy as np 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr01 = np.concatenate((arr1,arr2))
arr04 = np.stack((arr1,arr2),axis=1)

print("concatenate arr1 and arr2 :\n",arr01)
print("stack arr1 and arr2 along axis 1 :\n",arr04)

arr3 = np.array([[1, 2], [3, 4]])

arr4 = np.array([[5, 6], [7, 8]])

arr02 = np.concatenate((arr3, arr4), axis=0)
arr03 = np.concatenate((arr3, arr4), axis=1)
print("concatenate arr3 and arr4 along axis 0 :\n",arr02)
print("concatenate arr3 and arr4 along axis 1 :\n",arr03)
arr5 = np.hstack((arr1,arr2))
print("stack arr1 and arr2 along row :\n",arr5)
arr6 = np.vstack((arr1,arr2))
print("stack arr1 and arr2 along coloum :\n",arr6)
arr7 = np.dstack((arr1,arr2))
print("stack arr1 and arr2 along depth :\n",arr7)


