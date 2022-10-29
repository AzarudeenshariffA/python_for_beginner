
# decorator enhance the functionality of other functions
# @ used for decorators

def decorators_function(any_func):
    def wrapper_function():
        print("this is awesome func")
        any_func()
    return wrapper_function

def func():
    print("this is func")

func = decorators_function(func)
func()
# this is awesome func
# this is func

# or 

def decorators_function(any_func):
    def wrapper_function():
        print("this is awesome func")
        any_func()
    return wrapper_function

@decorators_function
def func():
    print("this is func")
func()
"""this is awesome func
this is func"""
@decorators_function
def func2():
    print("this is func2 ")
func2()
"""this is awesome func
this is func2"""