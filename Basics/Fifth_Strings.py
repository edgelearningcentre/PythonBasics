# ! Python3

# Strings can be indexed with the first character having index 0 






word = 'Python'
print(type(word))
# +ve indexing       012345        -----> left to right 
# -ve indexing      -6-5-4-3-2-1   <----   right to left

# extract letter y from variable word using + ve indexing
#print(word[4])


# extract letter p from variable word using -ve indexing 
print(word[-6])

print("end of testing ")


# extracting  letter y from the word Python 
print(word[1])      # +ve indexing
print(word[-5])     # -ve indexing

# for +ve values it starts from left to right P is having index 0 and n is having index value 5
# for -ve values it starts from right to left n is having -1 


#-----------------------------------------------------------

# Slicing allows us to obtain substring from  the main string

sentence = "Python Basics are the foundation concepts"
        #   012345 for Python
        #   6 for blank space
        #   7-13 for Basics

# extracting python word from the sentence :
substring = sentence[0:8]   # start number or index is included and end number  is excluded

print("testing of indexing******",substring)


# extracting Basics word from the sentence
substring1 = sentence[7:13]
print("extracting basics word--->",substring1)

# extract only foundation from sentence variable using +ve indexing and -ve indexing 

extract_found = sentence[-19:-9]   # -ve indexing 
extract_found_pos = sentence[21:32] # +ve indexing
print("extractdfoundation-->",extract_found)
print("extractdfoundation+ve-->",extract_found_pos)


# extracting the whole word from starting index value
substring2 = sentence[13:]
print("Sentence==>",sentence)
print("whole word===>",substring2)


# String is Immutable means not interchangable 

string1 = 'Python is the powerful language'        # we want to change letter P to C: it is not possible in case of strings

string2 = " Python and Java"
# print(string1[0]='P')


# f- string property in strings

new_string = f'{string1}{string2}'

print("printing data using f string",new_string)


"""
I have a string variable called s= 'I have 200 fingers'. wrong statement
I have a string variable called s= 'I have 10 fingers'. correct statement
replace incorrect words in original strong with new ones
replace property is used.
"""

person_vitals= 'I have 200 fingers' 

# replace  is a inbuilt function to replace string values

s1 = person_vitals.replace('200','10')
print("incorrect statement ",person_vitals)
print("correct statement",s1)  # first way

# print(person_vitals.replace('200','10')) # second way


