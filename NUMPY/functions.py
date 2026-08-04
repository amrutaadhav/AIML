#access element
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[1])
print(arr[3])
print(arr[-1])

#fancy
#print(arr[[1,2,4]])


#filtering
#print(arr[arr>25])

#slicing
print(arr[1:4])
print(arr[:4]) # 4 index print nhi hoga
print(arr[::2]) #2 sarakhe ghetlyavr tyat alternate print honar
print(arr[::-1]) #reverse print honar

#reshaping and manupulating
arr_2d = np.array([[110,20,46,35],[30,35,23,56]])
view
print(arr_2d.ravel())
copy
print(arr_2d.flatten())

# #reshaping
import numpy as np
arr=np.array([10,20,30,40,50,60])
reshaped_array = arr.reshape(2,3)
print(reshaped_array)

#handle missing values
import numpy as np

arr = ([1,2,3,4,np.inf,-np.inf,5,6,7])
print(np.isinf(arr))

arr = np.array([1,2,4,np.nan,9,-np.nan])
print(np.isnan(arr))

arr = np.array([2,4,np.nan,7,3,np.nan])
cleaned_nan = np.nan_to_num(arr,nan=90)
print(cleaned_nan)

arr = np.array([np.inf,8,4,5,np.inf,45,34,-np.inf])
print(np.isinf(arr))
cleaned_inf = np.nan_to_num(arr,posinf=100,neginf=900)
print(cleaned_inf)


#operations addition
import numpy as np 

arr1 = np.array([[1,3,4,5],[6,7,8,9]])
arr2 = np.array([1,2,3,4])
print("result:" , (arr1+arr2))


#problem
prices = [100,200,300]
discount = 10
final_prices = []

for price in prices:
  final_price = price - (price*discount/100)
  final_prices.append(final_price)
print(final_prices)


 

