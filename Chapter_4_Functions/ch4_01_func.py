# we used function before
# eg: len()
# always use Dry principle (Do not repeat yourself)
# kiss principle (keep it simple stupid)
'''
there are two types of function 
1) build in function
2) user defined function (we user def to create a function)
'''

# user defined function
# return is used to return a value from the function and we store it in a variable
# syntax
'''
def sum():  #function declaring
    code
sum() #function calling

# parameter and argument 
def sum(parameter):  #function declaring
    code
sum(argument) #function calling

'''
# sum of two numbers 
def sum_of_num(a,b): #function declaring
    return a+b

print(sum_of_num(5,4)) # --> 9 #function calling

# function using print

def add_num(a,b,c): 
    print(a+b+c)
add_num(2,3,4) # 9

# function using return 

def add_num(a,b,c):
    return (a+b+c)
print(add_num(2,3,4)) # 9


# Function practice

# Examples
# print last char
def last_char(name):
    print(name[-1])
last_char("azar") #r

# odd even 
def odd_even(num):
    if(num%2==0):
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")

odd_even(1)

# another way
def odd_even(num):
    return num%2==0
print(odd_even(4))


# greatest of three number 

def find_greatest(a,b,c):
    if(a>b) and (a>c):
        print(f"{a} is greater")
    elif(b>a) and (b>c):
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")
find_greatest(4,5,7)

# function calling another function

def greater(a,b):
    if (a>b):
        return a
    else:
        return b

def greatest_from_func(a,b,c):
    big = greater(a,b)

    return greater(big,c)

print(greatest_from_func(2,3,4))

# default parameter

def user_info(name="unknown",age=0):
    print(f"the user name is {name} and age is {age}")

user_info()

# global and local variable
x = 5  # global variable (we can use where ever we want)
def add():
    x = 10  # local variable (we can use var inside function only)
    print(x)  # 10
add()
print(x)  # 5



