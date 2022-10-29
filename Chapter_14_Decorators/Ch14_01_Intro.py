# you have to completely understand functions 
# first class function/ closures 
# at last decorators 

def square(a):
    return a**2
s = square
# we are assigning suare to s, so we can call function through s also 
print(s(7)) # 49

# to know the function actual name 
print(s.__name__) # square
print(square.__name__) # square
print(s) # memory location
print(square) # memory location

# pass function as arguements
# map example and working
l = [1,2,3,4,5]
def sq(n):
    return n**2
sq_Store = list(map(sq,l))
print(sq_Store)  # [1, 4, 9, 16, 25]

# simple method working of map 
l = [1,2,3,4,5]
def my_map(func, n):
    new_list=[]
    for i in n:
        new_list.append(func(i))
    return new_list
def sq(n):
    return n**2
print(my_map(sq,l)) # [1, 4, 9, 16, 25]

# using list comprehension 
l = [1,2,3,4,5]
def sq(n):
    return n**2
sq1 = [sq(i) for i in l]
print(sq1) # [1, 4, 9, 16, 25]

# using lambda
l = [1,2,3,4,5]
def my_map(func, n):
    new_list=[]
    for i in n:
        new_list.append(func(i))
    return new_list
sq2=my_map(lambda i : i**2, l) # [1, 4, 9, 16, 25]
print(sq2)

# function returning function 

def out_func():
    def inside_func():
        print("hello world")
    return inside_func

var = out_func()
var() # hello world

def out_side(msg):
    def inside_func():
        print(f"message is {msg}")
    return inside_func

var = out_side("hello...")
var() # message is hello...

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power

cube = to_power(3)
print(cube(2)) # 8

square = to_power(2)
print(square(2)) # 4

