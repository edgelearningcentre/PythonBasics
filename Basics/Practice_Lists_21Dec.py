# ! Python3 

# Task 1

# Write a python program to swap  (interchange) first and last element of the list

# input : [ 12,35,9,56,24]
# expected output : [24,35,9,56,12]



newList = [ 99,35,9,56,10]
print("original list",newList)

newList[0],newList[-1] = newList[-1],newList[0]
print("swapped list",newList)



# using pop command

first = newList.pop(1)
last = newList.pop(-2)

newList.insert(0,last)
newList.append(first)

print("using pop command",newList)




# Task 2 Find Maximum of two numbers in Python

# Input = [2,4]
# output = 4
# [1,2,5,7,8,82,99,15,6,7]
# hint : Use sort command  

max_two_numbers =  [2,4]
print(max_two_numbers)
max_two_numbers.sort()  # [1,2,5,6,7,7,8,15,82,99]  # ascending order
print("max number is:",max_two_numbers[-1])

max_two_numbers1 = [2,4] #[1,2,5,7,8,82,99,15,6,7]

# descending
max_two_numbers1.sort(reverse=True)  # [99,82,15,8,7,7,6,5,2,1]  # descending order
print("max number is descending order:",max_two_numbers1[0])

# max_two = max(1,2,5,7,8,82,99,15,6,7)  # inbuilt function in python to get the maximum number
# print(max_two)