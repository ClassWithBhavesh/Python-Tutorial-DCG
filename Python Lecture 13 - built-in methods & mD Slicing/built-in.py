# np.insert(arr, ind, value, axis=?)

import numpy as np
arr = np.arange(12)
print(arr)
# new_arr = np.insert(arr, [3, 5,8], 66)
# new_arr = np.insert(arr, 3,8, 66)
# new_arr = np.insert(arr, len(arr), 66)
# print(new_arr)
# print(arr)

# copied_array = np.append(arr, [66, 58])
# print(copied_array)


# new_arr = np.delete(arr, [5,7])
# print(new_arr)





nawa_arr = np.arange(36).reshape(3,2,6)

print(nawa_arr)

nawa_nawa_arr = np.insert(nawa_arr, 1, 99, -2)
print(nawa_nawa_arr)
