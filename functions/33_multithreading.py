import threading

def print_using_for(num):
    for i in range(1,num+1):
        print(i)


def print_using_while(num):
    i =1
    while i <= num:
        print(i)
        i+=1

# print_using_for(10)
# print_using_while(5)

t1 = threading.Thread(target=print_using_for,args=(10,))
t2 = threading.Thread(target=print_using_while,args=(10,))

t1.start()
t2.start()

# t1.join()
# t2.join()