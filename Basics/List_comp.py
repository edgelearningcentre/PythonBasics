# i =1 print odd
# i =2 print even

# lisst = ["Even" if i % 2 == 0 else "odd" for i in range(1, 21)]
# print(lisst)

## To print even numbers
# [2, 4, 6, 8 - --20]
# lisst = [i for i in range(1, 31) if i % 2 == 0]
# print(lisst)


startnum = 3
endnum = 100
lisst = [i for i in range(startnum, endnum + 1) if i % 2 == 0 and i % 3 == 0]
print(lisst)
