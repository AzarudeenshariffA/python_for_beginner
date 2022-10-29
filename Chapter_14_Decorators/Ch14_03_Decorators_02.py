# to take input from func we use args and kwargs

def decorator_function(any_fun):
    def wrapper_fun(*args, **kwargs): 
        print("hello")
        any_fun(*args, **kwargs)
    return wrapper_fun

@decorator_function
def func(n):
    print(f"the num is {n}")
func(5)
'''hello
the num is 5'''

# what if func returns 

def decorator_function(any_fun):
    def wrapper_fun(*args, **kwargs): 
        print("hello")
        return any_fun(*args, **kwargs)
    return wrapper_fun

@decorator_function
def func(a,b):
    return f"the num is {a+b}"
print(func(5,4))
'''hello
the num is 9'''


# <----------- decorators ------------>

def decorator_function(any_fun):
    def wrapper_fun(*args, **kwargs): 
        '''this is wrapper function'''
        print("hello")
        return any_fun(*args, **kwargs)
    return wrapper_fun

@decorator_function
def add(a,b):
    '''performs addition'''
    return f"the num is {a+b}"
print(add(5,4))

print(add.__name__)
print(add.__doc__)
'''wrapper_fun
this is wrapper function'''


# to see func 
from functools import wraps
def decorator_function(any_fun):
    @wraps(any_fun)
    def wrapper_fun(*args, **kwargs): 
        '''this is wrapper function'''
        print("hello")
        return any_fun(*args, **kwargs)
    return wrapper_fun

@decorator_function
def add(a,b):
    '''performs addition'''
    return f"the num is {a+b}"
print(add(5,4))

print(add.__name__)
print(add.__doc__)

"""add
performs addition"""