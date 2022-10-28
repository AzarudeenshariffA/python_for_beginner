# it is introuced in python first 
# function defined in one line also know as anonymous function 
# we usually use lambda function with build in function eg map,reduce and ect..

# example 


# simple method 
def add(a,b):
    print(a+b)
add(4,5) # 9
# lambda function
add = lambda a,b : a+b
print(add(3,4)) # 7

# practice
# simple method 
def is_even(a):
    print(a%2==0)
is_even(2) # True

# lambda function
ev = lambda a : a%2==0
print(ev(4)) # True

# last char
# simple method 
def char(a):
    print(a[-1])
char("azar") # r
# lambda function
last_char = lambda a:a[-1]
print(last_char("Azar")) # r

 
# IF ELSE WITH LAMBDA 
# syntax --> s = lambda(no of args):output if condition else output
# simple method 
def func(s):
    if(len(s)<5):
        return True
    else:
        return False
print(func("azarudeen")) # False
# lambda function
if_el = lambda s:True if len(s)<5 else False 
print(if_el("azar")) # True
