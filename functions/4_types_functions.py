# """
# without parameters, without return
# with parameters, without return
# without parameters, with return
# with parameters, with return
# """

# def addition(n1,n2):   # parameters
#     total = n1 + n2
#     print(total)

# addition(7,8) # (7,8) are positional arguments

def addition_list(x):
    total = 0
    for i in x:
        total = total + i
    print(total)

my_list =[100,200,300,400,500,600,700000,7654321000000000]


addition_list(my_list)