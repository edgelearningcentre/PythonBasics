# Lambda functions = Anonymous

# add_numbers = lambda n1,n2,n3: n1+n2+n3

# print(add_numbers(10,20,30))

# def add_numbers(n1,n2,n3):
#     return n1+n2+n3

# result = add_numbers(10,20,30)
# print(result)


# Take a argument which will be a number
# make a list from 0 to N

make_list = lambda n : [i for i in range(0,n+1)]

length = int(input("Enter length = "))

list1 = make_list(length)
list2 = make_list(15)

print(f'{list1=}')
print(f'{list2=}')