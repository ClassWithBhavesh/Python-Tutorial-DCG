# set in python - collection of unique elements (duplicate ele are not allowed)


# li = ["Bhavesh",20,True,60]
# print(li)

# vari = {"Bhavesh",20,True,60}
# print(type(vari))
# print(vari)




# # alternatic way to declare a set
# empty_set = set({10,20,50,60})
# print(empty_set)


# Methods in Set - add, remove, discard
# empty_set.add(98)
# print(empty_set)

# empty_set.discard(98)
# print(empty_set)

# empty_set.remove(98)
# print(empty_set)






# Operations in Set - union, intersection, difference, symmetric difference

setA = {1,2,3,4}
setB = {3,4,5,6}

# new_set = setA.union(setB)
# print(new_set)
# print(setB)

# new_set = setA.intersection(setB)
# print(new_set)
# print(setB)

# new_set = setA.difference(setB)
# print(new_set)
# print(setB)

new_set = setA.symmetric_difference(setB)
print(new_set)
print(setB)


