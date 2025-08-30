# ! python 3

# my_list = [1,2,3,'abc',2.5]

# print(my_list)


# empty_list = []

# print(empty_list)



# list constructor


# print(list(range(1,11)))


a = list((1,2,3))
# a1 = (1,2,3)
# print(type(a1))
b = list((4,5,6))
# print(a)
# print(b)





# print(a[0:2])   # 0 index value and 1 index value. 2nd index value is not included 

# print(len(a))
# print(a[4])



# create a list  A having numbers from 1,20 using range statement
# create a list  B having numbers from 21,40 using range statement

# create a list C by adding elements of list A and list B (Combine)

# A = list(range(1,21))
# B = list(range(21, 41))
# A.extend(B)
# print(A)



#a.pop() # to remove a last element of a list  answer is a [1,2]
# print(a)
# a.pop(0) # pass the index value to delete/ remove the specific element from a list
# print(a)
# a = [2,3]  # remove the first value as we are passing the index value 0 ( i.e. first element)


# remove duplicates from a list

# A = [1,1,2,2,3,4,5]

# print(type(A))

# B = set(A)   # set command is used to remove the duplicates values  or to get the unique values from a list

# sets are collection of objects, like lists but can only contain one of each element. 

# print(B)  # [1,2,3,4,5]


# print(type(B))   # list ----> set 

# # Counting element occurence in a list

# C = [1,2,1,4,1,7]
# print("actual values of list C",C)
# print(C.count(2))


print("sorting discussion")
# sorting -- ascending and descending

students = ['Adam','Ameen','Neeraj','John','Nick']
print("before sorting", students)
students.sort()
print("descending", students)



# it is applicable on the strings as well as on the numbers.
# letters = ['a','f','t','e','p']
# print("before sorting", letters)
# letters.sort(reverse=True)
# print("descending", letters)



# D = [10,2,5,4,2]   # default value is ascending
# print("before sorting",D)
# D.sort()
# print("ascending",D)  # [2, 2, 4, 5, 10]

# E = [10,2,5,4,2]   # when reverse= True it works as  descending
# E.sort(reverse=True)
# print("descending",E)


# # sorted() 

# F = [10,2,5,4,2] 
# print("before applying sorted",F)
# F1 = sorted(F,reverse=True)
# print("after applying sorted",F1)



#----------------------------------------------------------------------------------------------------------------


# create a new list having numbers 1 to 10 
# print the original list  A

# Get the first three elements of a list---> B
# print the modified list  B

# Get the last five elements from a list ---> C
# print the modifed list  C

A = [34,25,65,76]

B = A[0:3]
print(" we are extracting first three elements " + str(B))
