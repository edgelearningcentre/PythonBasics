"""
Ask 2 numbers from user.
calculate total of 2 numbers. 
print if the sum is odd or even

2 functions - add() , check()
"""


def add (n1,n2):
    total = n1 + n2
    return total


def check(num):
    if num %2 ==0:
        print("Even")  or return "Even"
    else:
        print("Odd")  or return "odd"


x = int(input("Enter number 1 :"))
y = int(input("Enter number 2 :"))
s = add(x,y)
check(s)


