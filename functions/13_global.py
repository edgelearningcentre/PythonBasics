a = 15


def change():
    global a 
    # local defined variable
    a =30
    print(a)

print(a)
change()
print(a)
