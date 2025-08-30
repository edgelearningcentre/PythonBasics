
# A tuple is a built in data type that allows to create immutable(unchangeable) sequences of values.

records = ('name','age','job')
# print(records)
# print(type(records))

# tuples are ordered, which means that they keep their elements in the original insertion order

record = ('Alice',23,'Python Developer')
# print(record)
# print(record[0])
# print(record[1])
# print(record[2])


# create an empty tuple
empty = ()                          #list1 = []
# print(empty)

# tuple constructor --- list  
# A = ("John",24,'Canada')                   
A = tuple(["John",24,'Canada'])     # tuple  from a list   () --- > []
            #[0],[1],[2]   for +ve indexing
            #[-3],[-2],[-1] for -ve indexing
# print(A)
# print(type(A))


# access its  values
new = tuple({                   # tuple from a dictionary  ()  --> {}
    'name': 'Alice',
    'age': 23,
    'job': 'Python Developer'}.items())

print(new)
# print(len(new))

# Access its elements by using -ve indexing
print(A[-1])



# tuple and we will extract its values by using slicing operator

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','cheatday')
# print(days)

# extract the first five elements 
# print(days[0:5])   # start index is included and end index is always excluded.
# print(days[:5])    # start index is 0 and end index is 5

# print(days[5:7])
# print(days[5:])

# Tuple immutability 

Students = ('Alice', 'Bob', 'Charlie')
# print(Students[2]=='Charlie')


# tuples don't support del statement on items 
# point = (7,14,21)
# del point[0]


# new tuple that are having a list inside a tuple





student_information = ("Neeraj",21,["Maths","Physics","History"],["Adam","USA","Devops","Java Developer"])
#print(student_information)

# update/ change the java developer to Data Scientist.
student_information[3][3] = 'Data Scientist'
# print(student_information)

# change/update its values 
student_information[2][2] = 'Science'
# print(student_information)



# creating copies of a tuple  Slicing operator
student_information_original = ("Neeraj",21,["Maths","Physics","History"],["Adam","USA","Devops","Java Developer"])
print("Original",student_information_original)
abc = student_information_original[:]                   
print("Hey i copied the whole tuple",abc)



# one another method copy function  Shallow

from copy import copy
def1 = copy(student_information_original)
print(def1)

# one another method deepcopy function

from copy import deepcopy
def2 = deepcopy(student_information_original)
print(def2)


# concatenation tuples --> joininig the tuples together

personal_info = ("John",35)

professional_info = ("computer science",("Python","Django","Flask"))

profile = personal_info + professional_info

print(profile)


tuple1 =(50,)
print(type(tuple1))


tuple1 = (11,22)
tuple2=  (99,88)
tuple1,tuple2 = tuple2,tuple1
print(tuple1)
print(tuple2)

tuple2 = tuple1[3:-1]