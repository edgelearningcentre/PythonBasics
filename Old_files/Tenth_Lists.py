'''
Python List, which can be written as a list of comma- separated values (items) between
square brackets. Lists may be contains different types, but usually contains have same type
'''

# Keshav having marks in different subjects
Marks = [45 , 56 , 48,  87, 76]
index = [0 ,   1  , 2,   3,  4] # it shows the positive index starts from LHS  0 to 5; Total 5 values
index = [-5,   -4,  -3, -2,-1]  # it shows the negative index starts from RHS -1 to -5; Total 5 values
firstindex = Marks[0]       # indexing returns the item from left is 45
print(firstindex)


negativeindex = Marks[-1]   # negative indexing returns the first element from Right is 76
print(negativeindex)

# slicing for subset of an list
subList = Marks[2:]
print(subList)    # It included the [2:] 2 means 2nd index and : means up to last value

# concatenation of lists
# if you want to add marks of other subjects in the existing list
Marks_updated = Marks + [65, 79]
print(Marks_updated)

# Unlike Strings, Which are immutable in nature, Lists are a mutable type
# Mutable : It is possible to change their content
squares_numbers = [1, 4, 9, 16, 26]     # the square of number 5 is 25, have entered wrong entry
squares_numbers[4] = 25                 # it replaces the 26 number with 25. 4 is index value of 26.
print(squares_numbers)

# To add new items in existing list. Use "append" method to do so.

squares_numbers.append(36)      # this will add 36 in the end of the list
print(squares_numbers)          # now the total entries are 6 and index starts from 0 to 5

# Slicing of an list is also possible, this can also change the size of the list

Room_items = ['A', 'B', 'C', 'D', 'E']
# replace some items with new values

Room_items[3:4] = 'F' # replace letter in 3 and exlcuded 4 value D is replaced with F value
print(Room_items)


