def add(x:int,y:int) -> int:
    total = x+ y
    return total


def greet(name:str,age:int,percentage:float) -> None:
    print(name)
    print(age)
    print(percentage)


print(greet("Neeraj",39,84.6))

c= add(10,20)
print(c)


# a =[58,74,14,25,56]

# a.sort()
# print(a)

# c = a.count(56)
# print(c)


from typing import List

def sum_of_list(x:List[int]):
    print(sum(x))

sum_of_list([10,20,30])
sum_of_list([100,200,300])