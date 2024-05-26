import numpy as np

arr=np.array([1,2,3,4,5])
print("array :",arr)
_0_D_arr=24
print("0-D array :",_0_D_arr)
_1_D_arr=np.array([1,2,3,4,5])
print("1-D array :",_1_D_arr)
_2_D_arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(_2_D_arr[1,-3])
print("2-D array :",_2_D_arr)
_3_D_arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12,]]])
print("3-D array : ",_3_D_arr)
print(_3_D_arr[1,0,1])
print(_3_D_arr.ndim,"- dimensional array ")
#5 dimensional array using ndmin argument
_5_D_array=np.array([[1,2,3,4,5],[6,7,8,9,10]],ndmin=5)
print("5-D array : ",_5_D_array)
#check dimensions of array[a.ndim]
print(_5_D_array.ndim,"- dimensional array ")
print(type(arr))
print("version :",np.__version__)







