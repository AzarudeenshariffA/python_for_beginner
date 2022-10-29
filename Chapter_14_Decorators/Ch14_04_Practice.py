"""
from ast import arg


def print_function_data(func):
    def wrapper_function(*args):
        print(f"you are calling {func.__name__} function ")
        print(f"you are calling {func.__doc__} ")
        return func(*args)
    return wrapper_function
@print_function_data
def add(a,b):
    '''this function takes two number ass atguement and returns the sum'''
    return a+b
print(add(5,4))
'''you are calling add function 
you are calling this function takes two number ass atguement and returns the sum
9'''

# excercise 1

# to calculate time 
import time
def time_take(func):
    def wrapper_func(*args):
        t1 = time.time()
        print(f"{func.__name__} is executing")
        return_f =  func(args)
        t2= time.time()
        print(f"the function take {t2-t1} time to execute")
        return return_f
    return wrapper_func

l = list(range(1,100000000))
@time_take
def sq(n):
    return [i**2 for i in l]
sq(100)
'''sq is executing
the function take 47.188783168792725 time to execute'''
"""
# practice 2
# only integer are allowed

from hashlib import new


def decorator_func(data_type):
    def only_fun(func):
        def wrapper_func(*args):
            new = []
            for i in args:
                new.append(type(i) == data_type)
            if all(new):
                return func(*args)
            else:
                return "invalid"
        return wrapper_func
    return only_fun


@decorator_func(str)
def fun(*n):
    new1 = []
    for i in n:
        new1.append(i)
    return new1


l = ["1", "2", "3", "4", "5", "6"]
print(fun(*l))
