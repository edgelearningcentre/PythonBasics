# def keyword introduces a function definition.
# It must be followed by the function name and parenthesized list of formal paramters

# Definition of an Function
def add_num(num1,num2):         # define two arguments for num1 and num2
    added = num1 + num2         # define expression for evaluation + , -, * or /
    print(' The total of two numbers is : ', added) # print the added output

# Calling of an Function with its required two arguments
add_num(5,7)        # 5 is assigned to num1 and 7 is assigned to num2
                    # the addition of 5 and 7 is 12 and stored in added variable

add_num(17,98)
add_num(23,65)


# Create a function that writes the Fibonnaci Series to an arbitary boundary

# Definition of a Function
def fibSeries(num):     # write Fibonnaci Series up to num numbers 
    num1,num2 = 0,1     # intially  num1 = 0 and num2 = 1
    while num1 < num:   # condition num1 is less than called number num
        print(num1, end = ' ')  # print first number with space as a  separator
        num1, num2 = num2 , num1 + num2     # show num2 and add num1 + num2 up to argument limit
        print()          # create a blank line with this function

# Calling of a Function with its required one parameter. In this num = 1000
fibSeries(1000)

# Write a program that returns and stores a list of numbers of the Fibonacci series.

def saveFibonnai(num):
    out_result = []     # Intialize an empty list. [] means list
    num1,num2 = 0,1     # intially  num1 = 0 and num2 = 1
    while num1 < num:   # condition num1 is less than called number num
        out_result.append(num1)     # append a empty list with the calculated values
        num1, num2 = num2 , num1 + num2     # show num2 and add num1 + num2 up to argument limit
        return out_result

# Calling of a Function
saveFibonnai(1000)
