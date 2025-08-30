# Fibonacci Series
# sUM OF two elements defines the next value 
FirstNumber, SecondNumber = 0 , 1
while FirstNumber < 10:
    print(FirstNumber)
    FirstNumber,SecondNumber = SecondNumber, FirstNumber + SecondNumber


'''
Above example shows some new features
1. First line contains multiple assignment.
2. RHS expressions are evaluated from the left to the right.
3. while loop executes as long as condition remains true. 
----> In Python, like in C, any non-zero interger value is true; Zero is false.
4. The body of the loop is "indented" is Python's way of grouping statements. 
'''