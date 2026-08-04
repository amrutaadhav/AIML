# delete
import numpy as np
arr_2d = np.array([[1,3,6,4],[7,6,4,5]])
new_arr_2d = np.delete(arr_2d,1,axis=1) #axis 0 means row , 1 means col
print(new_arr_2d)

# element
new_array = np.delete(arr_2d,2)
print(new_array)