# Broadcasting in Python

# using python lists -

# prodPricing = [199, 4999, 11000]
# discount = 30

# finalProdPrice = []

# for price in prodPricing:
#     priceAfterDis = price - (price * discount/100)
#     finalProdPrice.append(priceAfterDis)

# print(finalProdPrice)




# using numpy arrays - 
# import numpy as np
# prodPrices = np.array([199, 4999, 11000])
# print(prodPrices)
# discount = 30

# new_prod_price = prodPrices - (prodPrices * discount / 100)
# print(new_prod_price)
# print(prodPrices)







# Vectorization - 

# li = [10,20,30,60]
# print(li)

# new_li = li ** 2
# print(new_li)

# num = 552
# print("the number is : ", num)



# numpy vectorization - 

import numpy as np

# arr = np.array([10,20,30,60])
# print(arr)

# new_arr  = arr ** 2
# print(arr)
# print(new_arr)



# broadcasting in numpy using 2D array - 

# arr = np.random.randint(2,50, size=(2,3))
# arr = np.random.randint(2,3,size=(2, 4))
# arr1 = np.arange(6).reshape(2,3)
# print(arr1)

# arr2 = np.arange(3)
# arr2 = np.arange(2)     # array compatibility matters in broadcasting
# print(arr2)


# new_arr = arr1 + arr2
# print(new_arr)




