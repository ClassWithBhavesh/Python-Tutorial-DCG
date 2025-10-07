# Handling missing and special values - 

import numpy as np
# empAge = np.array([np.nan,42,np.nan,52, np.nan])

# how to indentify or find the nan value:
# print(np.isnan(empAge))
# print(empAge)

# replace the nan value from our dataset:
# cleaned_arr = np.nan_to_num(empAge, nan=45)

# print(empAge)
# print(cleaned_arr)




# creating an infinite array or infinite values - 

# empAge = np.array([np.inf,42,np.inf,52, -np.inf])
# print(empAge)
# identifying the infinite value in a given array - 
# print(np.isinf(empAge))

# replacing of infinite values from an array -
# new_arr = np.nan_to_num(empAge, posinf=12, neginf=20)
# print(new_arr)








# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# print(arr)
# even_arr = arr[arr%2 == 0]
# greator_than_5_arr = arr[arr > 5]
# print(greator_than_5_arr)



