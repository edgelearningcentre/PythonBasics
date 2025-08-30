# Nested loops


"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

"""
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()

#-----------------------------------------------

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

"""
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

#-----------------------------------------------


"""
5 4 3 2 1 
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
"""
# for i in range(5,0,-1):
#     for j in range(5,0,-1):
#         print(j,end=" ")
#     print()
#-----------------------------------------------


"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()

#-----------------------------------------------


"""
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
"""
# for i in range(5,0,-1):
#     for j in range(5,0,-1):
#         print(i,end=" ")
#     print()

#-----------------------------------------------

"""
Ask N from the user: N means number of lines for e.g.5 

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
# num = int(input("Enter a number for a pattern = "))

# for i in range(1,num+1):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()

#-----------------------------------------------

"""
1
1 2
1 2 3 
1 2 3 4
1 2 3 4 5 
"""

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#-----------------------------------------------

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#-----------------------------------------------
"""
1
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
"""
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
#-----------------------------------------------

"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
# for i in range(6,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()
#-----------------------------------------------
"""
5 4 3 2 1
5 4 3 2
5 4 3 
5 4 
5

"""
# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()

#-----------------------------------------------

"""
5 4 3 2 1
4 3 2 1
3 2 1 
2 1 
1
"""

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

#-----------------------------------------------


"""
q q q q *
q q q * * 
q q * * *
q * * * *
* * * * *

"""
# for i in range(1,6):
#     for j in range(i,5):
#         print("q",end=" ")

#     for k in range(1,i+1):
#         print("*",end=" ")

#     print()

#-----------------------------------------------
"""
q q q q *
q q q * * *
q q * * * * *
q * * * * * * * *
* * * * * * * * * *
"""
# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")

#     for k in range(0,(i*2)-1):
#         print("*",end=" ")

#     print()

#-----------------------------------------------
# Diamond Shape 
for i in range(1,6):
    for j in range(i,5):
        print(" ",end=" ")

    for k in range(0,(i*2)-1):
        print("*",end=" ")

    print()

for i in range(4,0,0-1):
    for j in range(5,i,-1):
        print(" ",end= " ")

    for k in range((i*2)-1):
        print("*",end = " ")
    print()