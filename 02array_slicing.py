import numpy

array1=numpy.array([0,1,2,3,4,5,6,7,8])
print("array1 index 1 to 3 = ",array1[1:3])
print("array1 index 1:5:2 =",array1[1:7:2])
print("array1 index ::2 ",array1[::2])

array2=numpy.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#prints index from second array
print("array2 index 1,0:4 =",array2[1,0:4])
#prints 2nd index form both array
print("array2 index 0:2,2 = ",array2[0:2,2])
#slice 1:4 from both elements
print("array2 index 0:2,1:4 =",array2[0:2,1:3])





