## Sets : To Store unique values , unordered and mutable

# does not store duplicate values
# not in an proper order
#  mutable : we can change its values
# iterbale hai
# it does not have any index or position of values


set1 = {4, 6, 4, 3, 4, 1, 5, 4, 3, 67, 66.77}
print(set1)


# Type conversion

set2 = [4, 6, 4, 3, 4, 1, 5, 4, 3, 67, 66.77]
print(set(set2))

# Methods of Sets
# Union : combine both sets and remove duplicates
# Intersection : common elements
set3 = {4, 6, 4, 3, 4, 1, 5, 4, 3, 67, 66.77}
set4 = {4, 5, 4, 3, 5, 1, 9, 4, 3, 65, 66.77}

print(set3.union(set4))
print(set3.intersection(set4))


set5 = [4, 6, 4, 3, 4, 1, 5, 4, 3, 67, 66.77]
set6 = [4, 6, 4, 3, 4, 1, 5]


set7 = {3, 4, 5, 6, 7, 8}
print(set7)
set7.add(9)
set7.remove(3)


## membership operators

set8 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

num = int(input("Enter a number = "))

if num in set8:
    print("yes")
else:
    print("no")

# found = False
# for i in set8:
#     if i == num:
#         found = True
#         print("yes")
# if found: 
#     print("Yes")
# else:
#     print("No")