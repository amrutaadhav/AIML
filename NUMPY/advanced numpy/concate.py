# concate
import numpy as np

arr = np.array([10,20,30,40])
arr1 = np.array([10,20,30,40,48,67])
new_array = np.concatenate((arr,arr1))
print(new_array)