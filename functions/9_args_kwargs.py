# def add(*args,**kwargs):
#     "arbitrary arguments use args(arguments) and kwargs(keyword arguments) "
#     # print(sum(args))
#     for k,v in kwargs.items():
#         print(k,v)
    # print(kwargs)


# args used when we dont know the no of parameters 
# add(name="neeraj",age=100,gender="Male")

# add([1,2],[100,200],45,100)
# add(1,2,3)
# add(100,5,6,5,4,9)
# add(12,24)


def add(n1,n2,n3,*args,**kwargs):
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args=}")
    print(f"{kwargs=}")
    print(f'{kwargs["name"]=}')

add(1,2,3,4,5,6, name="neeraj")