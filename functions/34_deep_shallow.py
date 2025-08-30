# a = [45,65,34,21]

# b =a 
# a[0] = 100
# print(id(a))   # to check the reference values 
# print(id(b))

import copy 

a = [[41,12,83],[44,35,16],[767,38,19]]

# b = a.copy()   # Shallow copy 

b = copy.deepcopy(a)


print(a)
print(b)

print("--------------------")

a[0][0] = 100

print(a)
print(b)