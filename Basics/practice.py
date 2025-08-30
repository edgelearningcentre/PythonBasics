# rows = 5
# for i in range(1,rows+1):
#         print("*" *i,end= "")
#         print()



# How do you implement memoization in Python to optimize
# recursive functions?
from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
 if n <= 1:
  return n
 return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10)) # Output: 55


# Create Generator
def countdown(n):
 while n > 0:
  yield n
  n-=1

gen = countdown(3)
# print(next(gen))

# Simple interable method
class Countdown:
 def __init__(self,n):
  self.n = n

 def __iter__(self):
  return self

 def __next__(self):
  if self.n <= 0:
   raise StopIteration
  self.n -=1
  return self.n + 1
 

it = Countdown(3)
for i in it:
 print(i)


#  How to use args and kwargs 
import functools

def logger_decorator(func):
 @functools.wraps(func)
 def wrapper(*args,**kwargs):
  print(f"Calling {func.__name__} with args:{args} and kwargs : {kwargs}")
  result = func(*args,**kwargs)
  print(f"{func.__name__} returned{result}")
  return result
 return wrapper

@logger_decorator
def compute_sum(a,b,c=2):
 return a+b+c

print(compute_sum(1,2,3))

#  How to perform custom aggregation
import pandas as pd

df = pd.DataFrame({
 'Department': ['IT', 'IT', 'HR', 'HR', 'Finance'],
 'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
 'Salary': [80000, 90000, 60000, 65000, 70000],
 'Bonus': [5000, 6000, 3000, 3200, 4000]
})