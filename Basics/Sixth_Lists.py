# ! Python3
"""
Python List, which can be written as a list of comma- separated values(items) between square brackets
for e.g. a= [1,2,'a',3.5]
"""
 # [1,2,'a',6,9,3.0,]

# Neeraj is having  marks in different subjects 

Marks = [45, 56 ,'abc', 48.5, 87.4, 76.8]     # class : int,float,str,list
print(type(Marks))
print()
# print(Marks)

print(Marks[3])

print()
# index for +ve [ 0 1 2 3 4]   ---> left to right 
# index for -ve [-5 -4 -3 -2 -1]  ---> right to left

firstindex = Marks[-1]
print("negative indexing",firstindex)

# Slicing for extract subset from an list
sublist = Marks[0:4]   # first number is included and last number is excluded   [0,1,2]
print("sublist of main list",sublist)

# concatentation of lists
print("original list",Marks)
Marks_updated = Marks + [65,79]
print("updated list",Marks_updated)

# Mutable property
# unlike strings, which are immutable in nature , Lists are a mutable type
# mutable : It is possible to change their items inside the list.

Square_numbers = [1,4,9,17,26]
                #[0,1,2,3,4]
                # change value 17 to 16 
Square_numbers[3] = 16
Square_numbers[4] = 25
print(Square_numbers)


# [1,4,9,16,25]   # we want to add 36 at the end of list
# append property
# Square_numbers.append(36)
Square_numbers = Square_numbers + [36]
print("after adding new number ",Square_numbers)

# # remove property
Square_numbers.remove(25)
print("after removing the item",Square_numbers)


# insert property
Square_numbers.insert(5,49)   # at index position 5 and adding 49 number.
print("after inserting with index value",Square_numbers)



Room_items = ['A','B','C','D','E']
             #[ 0,  1 , 2 , 3 , 4]
#Room_items = [A,B,C,D] we cannot define strings with quotes inside the list, it gives Name error

# replace the value D with F 
Room_items[3] = 'F'

s1 = Room_items.replace('D','F')     # replace command is only applicable on strings
print("original list",Room_items)
print("Updated list",s1)




# li = [2200,2350,2600,1930,2190]
# print("first element",li[0])
# print(f'{li[0]},{li[1]},{li[2]}, subtraction of extra dollars are : 2130-200={li[3]},{li[4]}')


