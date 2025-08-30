# Lists: To Store multiple values in a single variable

# a = [54, 65, 11, 91, 88,45,32]
# print(a)

## Iterate by index or position

# for i in range(0,len(a)):
#     print(a[i])

## Iteration by values.py
# for i in a:
#     print(i)


# Print list in reverse
# my_list = [4, -98, "Neeraj", 22.22, 100]

# for i in range(len(my_list)-1, -1, -1):
#     print(my_list[i], end=" ")

# 100 22.22 Neeraj -98 4

## Print all the even numbers present in the list

# check_odd_even = [3,4,6,100,887,337,10,24,78]
# Iteration by index

# for i in range(0,len(check_odd_even)):
#     if check_odd_even[i]%2==0:
#         print(check_odd_even[i],end=" ")

# Iteration by value
# for i in check_odd_even:
#     if i%2==0:
#         print(i,end=" ")


## Print all the elements present at even index position

# for i in range(0,len(my_list)):
#     if i%2==0:
#         print(my_list[i],end=" ")

## Print the sum of all elements present in that list

# my_list = [51, 85, 91.66, 52, 44, 100, 200]

# Iterate by index
# summ = 0
# for i in range(0,len(my_list)):
#     summ = summ + my_list[i]
# print(summ,end=" ")


# Iterate by value
# summ = 0
# for i in my_list:
#     summ = summ + i
# print(summ,end=" ")


# -------------------------------

## Print the count the numbers of even numbers present in list
# my_list = [3, 4, 6, 100, 887, 337, 10]

# count = 0
# for i in range(0, len(my_list)):
#     if i % 2 == 0:
#         count = count + 1
# print(count, end=" ")
# -------------------------------


## Print the largest number present in the table
# my_list = [3, 4, 6, 100, 887, 337, 10]

# largest = 0

# for i in range(0, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]

# print(largest, end=" ")

# -------------------------------
# my_list = [-3, -4, -6, -100, -887, -337, -10]

# largest = my_list[0]

# for i in range(0, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]

# print(largest, end=" ")

# -------------------------------

# my_list = [-3, -4, -6, -100, -887, -337, -10]
# my_list.remove(-3)
# print(my_list)

# del my_list


# -------------------------------
# list_length = int(input("Enter length = "))

# result = []

# for i in range(0, list_length):
#     num = int(input(f"Enter a number at position {i} = "))
#     result.append(num)

# print(result)

# -------------------------------

# new_list = [5,10,15,20,15]
# old_number = 15
# new_number = 25

# for i in range(0,len(new_list)):
#     if new_list[i] == old_number:
#         new_list[i] = new_number


# print(new_list)

## Remove all even numbers from the list

# lisst = [45, 66, 66, 66, 66, 66, 78, 11, 12, 12, 12]
# ll =[]
# for i in lisst:
#     if i % 2 == 1:
#         ll.append(i)

# print(ll)


## remove all the duplicates element from that list
# lisst = [45, 66, 66, 66, 66, 66, 78, 11, 12, 12, 12]
# result = []

# for i in lisst:
#     if i not in result:
#         result.append(i)

# print(result)

## Make a list. then ask a number from a user. If number exists
## in that list then print the position of the element else print -1

# lisst = [5, 1, 5, 10, 20, 5, 1, 1]
# num = int(input("Enter a number = "))


# if num in lisst:
#     index = lisst.index(num)
#     print(f"Index = {index}")

# else:
#     print("-1")
# for i in range(0,len(lisst)):
#     if lisst[i]==num:
#         print(i)
#     else:
#         print("-1")


# Reverse a list
# result = []
# for i in range(len(lisst)-1,-1,-1):
#     result.append(lisst[i])
# print(result)


## To find the occurence of each element in a list and print
## the element with the highest occurence.

# lisst = [5, 1, 5, 5, 6, 1, 3]

# result = []
# for num in lisst:
#     if num not in result:
#         result.append(num)

# for i in result:
#     c = lisst.count(i)
#     print(f"{i} occurs {c} times")

## To find the second largest number in the list without sorting

# lisst = [ 54,32,17,67,43,11,87,44,54,32]

# largest_number = float("-inf")
# second_largest = float("-inf")

# for num in lisst:
#     if num > largest_number:
#         second_largest = largest_number
#         largest_number = num
#     elif num > second_largest and num < largest_number:
#         second_largest = num

# print(second_largest)

## Takes a list of integers and returns the product of all the elements

# lisst = [41, 87, 85, 44]

# product = 1

# for num in lisst:
#     product = product * num

# print(product)

## To find and print all prime numbers within a given list

lisst = [2, 5, 7, 8, 9, 10, 11, 13, 17]

for num in lisst:
    factors = 0
    for i in range(1,num + 1):
        if num % i == 0:
            factors = factors + 1
    if factors == 2:
        print(num)
