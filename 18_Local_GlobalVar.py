# Run this program you will get error !
def Sum():          # Definition of a function with blank argument name
    var1 = 123456   # define variable named var1 
    #print(var1)    # acts as a local varible inside function def.

Sum()               # call sum function
print(var1)         # acts as a global variable outside function def.

# To print the var1 values : use print(var1) inside the definition of function 
# and re-run the program and just uncomment the line 4 and put comment on line 7

'''
Error 
Traceback (most recent call last):
  File "c:/Users/PythonBasics/18_Local_GlobalVar.py", line 5, in <module>
    print(var1)
NameError: name 'var1' is not defined
'''
# Global Statement
def sub():
  global word   # define word variable in a global scope using keyword 'global'
  word = 'Hello'

word = 'Daniel'

sub()
print(word)   # print the value of variable word 
