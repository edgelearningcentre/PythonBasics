# First Var

prefix = 'Python'
#prefix 'language' # cant concatenate a variable and a string variable

'''
File "c:/Users//PythonBasics/Seventh_Concatenate.py", line 4
    prefix 'language' # cant concatenate a variable and a string variable
           ^
SyntaxError: invalid syntax
'''
# to run the program just comment the line 4 
output = prefix + 'language'
print(output)



# Strings can be indexed (subscripted) with the first character having index 0 

word = 'Python is a powerful language'
print(word[0])      # character in index value 0 is P
print(word[5])      # character in index value 5 is n 

# indices  may also be negative numbers , start counting from right hand side

print(word[-1])      # character in index value -1 is e
print(word[-5])      # character in index value -5 is g
