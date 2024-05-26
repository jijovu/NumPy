import numpy as np

arr1 =np.array([1,2,3,4,5,6])
arr2 =np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
arr3 =np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])

arr01 = np.array_split(arr1,3)
arr02 = np.array_split(arr1,4)
arr03 = np.array_split(arr2,2)
arr04 = np.array_split(arr2,2,axis=1)
arr05 = np.dsplit(arr3,3)

print("spliting arr1 into 3 :\n",arr01)
print("first array inside arr01 :\n",arr01[1])
print("spliting arr1 into 4 :\n",arr02)
print("spliting arr2 into 3 :\n",arr03)
print("spliting arr2 into 3 along rows :\n",arr04)
print("spliting arr2 into 3 along heingt :\n",arr05)




