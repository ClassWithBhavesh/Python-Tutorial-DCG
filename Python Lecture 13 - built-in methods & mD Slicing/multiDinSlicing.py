# Slicing in Multi-Dimensional Array - 

# import numpy as np

# arr = np.arange(12).reshape(2,2,3)
# print(arr)
# new_arr = arr[1, 0, 0:3]
# new_arr = np.array([arr[0,0,0:3], arr[1,0,0:3]])
# new_arr = np.concatenate((arr[0,0,0:3], arr[1,0,0:3])).reshape(2,3)
# new_arr = arr[:,0,:]
# print(new_arr)


"""
    [[8 2]
     [11 5]]
"""

# ran_arr = arr[:, :, -1]
# print(ran_arr)
# des_arr = np.transpose(ran_arr)
# print(des_arr)
# des_arr = np.flipud(ran_arr)
# print(des_arr)


# ran_arr = np.array([[arr[1,0,2],arr[0,0,2]], [arr[1,1,2], arr[0,1,2]]])
# in_arr = ran_arr[::-1, ::-1]
# re_in_arr =in_arr[::1, ::1]
# print(ran_arr)
# print(in_arr)
# print(re_in_arr)












