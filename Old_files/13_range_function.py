# if you do need to iterate over a sequence of  numbers.
# range function generates arithemtic progressions

for i in range (0,10):      # end point is never part of the generated sequence.
    print(i)                
"""
Output
0
1
2
3
4
5
6
7
8
9
"""

new = list(range(5,10))     # it generates number between 5 and 10 and converted into list
print(new)                  # it displays all the values of new variable
print(type(new))            # it shows the type of new variable i.e. is List

"""
Output
[5, 6, 7, 8, 9]
<class 'list'>
"""

new1 = list(range(0,10,2))     # it generates number between 0 and 10  with increment of 2 and converted into list
print(new1)                  # it displays all the values of new variable
print(type(new1))            # it shows the type of new variable i.e. is List

"""
Output
[0, 2, 4, 6, 8]
<class 'list'>
"""

# To iterate over the indices of a sequence, we can combine range() and len() 
Student_Names = ['Ravinder', 'Gurpreet','Raman','Shivinder']
for name in range(len(Student_Names)):
    print(name, Student_Names[name])

"""
Output
0 Ravinder
1 Gurpreet
2 Raman
3 Shivinder
"""


# Strange thing about range function
r = range(10)
print(r)

sum_range = sum(range(4))  # it adds 4 values  0 + 1 + 2 + 3 = 6
print(sum_range)
