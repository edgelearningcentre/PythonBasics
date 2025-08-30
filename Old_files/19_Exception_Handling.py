# Getting an error, or exception, in your Python program means
# the entire program will crash. 
# We want the program to detect and handle them with out

def errorbyzero(num,divby):         # definition of function
    try:                            # try with below instructions
        return num/divby
    except ZeroDivisionError:       # except the following errors
        print("Invalid Value")      # print the statement

print(errorbyzero(40,0))
print(errorbyzero(40,8))
