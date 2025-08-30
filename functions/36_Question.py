"Write a python decorator that measures the time a function takes to execute."
" Ensure it works for functions with any number of arguments"


from datetime import datetime
from time import sleep

def cal_time(func):
    def wrapper(*args):
        start_time = datetime.now()
        func(*args)
        end_time = datetime.now()
        print(end_time-start_time)

    return wrapper


@cal_time
def add(*args):
    print(sum(args))

# add(5,10,40,58)
add(list(range(1,1000)))
