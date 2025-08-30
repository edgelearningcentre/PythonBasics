#1) Write code that prints Python if 1 is stored in Var, prints Basics if 2 is
# stored in Var, and prints Greetings! in Python Basics if anything else is stored in Var.


Var = input("Enter a number : ")
print(Var)
if Var == '1':
   print('Python')
elif Var == '2':
   print('Basics')
else:
   print('Greetings ! in Python Basics')
          
#2) Write a short program that prints  the numbers 1 to 10 using a for and while loop.

##for i in range(1,11):
##    print(i)
##    i += 1

i = 1
while i < 11:
    print(i)
    i += 1
