"""
The break statement, breaks out of the innermost enclosing for or while loop
Loop is terminated by a break statement
"""
# Prime Number 
for i in range(2,10):
    for j in range(2,i):
        if i % j == 0:          # condition for prime number 
            print(i,'equals',j,'*',i//j)
            break
        else:
            print(i, ' is a prime number')

# The Continue statement, continues with the next iteration of the loop

for num in range(2,10):
    if num % 2 == 0:
        print('Found Even Number',num)
        continue 
    print('Found Odd Number', num)