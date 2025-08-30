
# Question 1 : Find the smallest and the largest list elements on input provided by the user.

# Question 2 : WAP to split a list in half and store the elements in two different lists.


list1 = [1,2,3,4,5,6,7,8,9,10]
half = len(list1)/2
# list1 = ['ABC',45,'xyz',44,'CDE',46,'xyzer',50]
print("first half is ",list1[:half])
print("second half is ",list1[half:])


# Question 3 : WAP to find the simple interest for given principal amount , rate  of interest and time provided by the user.

# Question 4 : WAP to find the area of a circle with radius provided by the user.


# Question 5 : WAP to remove empty list from a given list 

list1 = ['ABC',[],'xyz',[]]
print(list1)

res_list = list(filter(None, list1))
print(res_list)


