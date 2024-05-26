import numpy as np

arr1 =np.array([1,2,3,4,5,6])
arr2 =np.array([[1,2,3],[4,5,6]])
arr3 =np.array([[[1,3],[3,4]],[[5,6],[7,8]]])

print("1-D array iterating :")
for x in arr1:
    print(x)

print("2-D array iterating :")
for y in arr2:
    for y1 in y:
        print(y1)

print("3-D array iterating :")
for z in arr3:
    for z1 in z:
        for z2 in z1:
            print(z2)

#iterate throungh array as string

for i in np.nditer(arr1,flags=['buffered'],op_dtypes=['S']):
    print(i)                           

arr4 =np.array([[1,2,3,4],[5,6,7,8]])

for j in np.nditer(arr4[:, ::2]):
    print(j)

arr5=np.array([1,2,3])

for idx,k in np.ndenumerate(arr5):
    print(idx,k)

for idx,a in np.ndenumerate(arr4):
    print(idx,a)




