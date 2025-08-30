

# Definition
"""
A Dictionary consists of collections of key-value pairs. Each key value pair maps the key to its associated value
"""

# Note : Dictionary by enclosing a comma separated list of key value pairs in curly braces {}

# Syntax 
# d = {
#         'key1':'value1',    # colon separates each key from its associated value
#         'key2':'value2',
#         'key3':'value3'
#     }


# create a dictionary of students and its class 

# Students = {
#         'John' : 'Nursery',
#         'Rocky': 'Ist',
#         'Jackson' : 'IInd'
# }

# print(Students)
# print(type(Students))


# 1 Accessing Dictionary Values
# A value is retrieved from a dictinary by specifying its corresponding key in square brackets ([]):

# First_key = Students['John']
# print(First_key)


# key_not_present = Students['Neeraj']
# print(key_not_present)


# 2 Adding an entry to an existing dictionary
# Students['Neeraj'] = 'IIIrd'
# print(Students)

# 3 update an entry (key/value pair)

# Students['Neeraj'] = '5th'
# print(Students)

# 4 To delete an entry, use del statement specifying the key to delete
# del Students['Neeraj']
# print(Students)



# Building Dictionary incrementally 
# personal_information = {}
# # print(type(personal_information))
# personal_information['First_Name'] = 'Adam'
# personal_information['Last_Name']  = 'Payz'
# personal_information['Age']        = 40
# personal_information ['Country']   = 'USA'
# personal_information ['Occupation'] = 'Software Engineer'
# personal_information ['Skills']    = ['Python','Devops','Java']      # give multiple values of a single key
# personal_information['Skills_Rating'] = {'Python': 'Beginner','Devops':'Advanced','Java':'Intermediate'}   # key is having multiple key-value pairs
# # print(personal_information)

# # Access its value 
# print(personal_information['Skills'])

# # want to access only specific value from a key , writing 0 to extract only  python value which is associated with key Skills # 64
# print(personal_information['Skills'][-1])

# # want to access specific value from a key  # 65
# print(personal_information['Skills_Rating']['Devops'])



##################------------------------------

# Restrictions on Dictionary keys 

# any type of value can be used as a dictionary key in python such as integer, float, string are used as keys

# 1) a given key can appear in a dictionary only once. Duplicate keys are not allowed. 

Students1 = {
        'John' : 'Nursery',
        'Rocky': 'Ist',
        'Jackson' : 'IInd',
        'John'    : 'IIIrd',
        'John' : '5th',
}
# print(Students1)

Students1['John'] = 'IIIrd'

# 2 ) A dictionary key  must be of a type that is immutable
# immutable --> which cannot be changed.


#--------------- Built in Dictionary Methods

# clear--> empties dictionary Students1 of all key value pairs
Students1.clear()
# print(Students1)


# get--> extracts the value for a key if it exists in the dictionary
Students2 = {
        'John' : 'Nursery',
        'Rocky': 'Ist',
        'Jackson' : 'IInd',
        'John'    : 'IIIrd',
        'John' : '5th',
}
# print(Students2.get('Jackson'))
# print(Students2['Jackson'])
# print(Students2['Adam'])   # None value as Adam key is not present in the dictionary


# items --> returns or gives us a list of key-value pairs in a dictionary

# print(Students2.items())
print(list(Students2.items()))     

print(list(Students2.items())[0][0])     # extract key having index value zero 
print(list(Students2.items())[0][1])    # extract  value having index value zero

print(list(Students2.items())[1][0])     # extract key having index value one 
print(list(Students2.items())[1][1])     # extract value having index value one 


print(list(Students2.items())[2][0])     # extract key having index value two 
print(list(Students2.items())[2][1])     # extract value having index value two 
# print(list(Students2.items()))     


