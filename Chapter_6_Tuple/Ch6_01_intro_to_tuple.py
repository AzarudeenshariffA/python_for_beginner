# tuple data structure
# tuple can store any data type
# most important tuples are immutable,once tuple is created we can't update
# no append, insert, pop, remove method will work
## use when we don't need to change data 
# eg:-
# var = (1,"2",3.1)

# methods we can use
# count, index, len, slicing
'''
# looping in tuples 
mix = (1,2,3,4,5,6)

for i in mix:
    print(i)
# tuple with one element
num = (1)
num1 = (1,)
print(type(num1)) # <class 'tuple'>
print(type(num)) # <class 'int'>

# tuples without paranthesis 
mix = 1,2,3,4
print(type(mix)) # <class 'tuple'>

# tuple unpacking 
fruit = ("Azar","mango","orange")
f1,f2,f3 = (fruit)
print(f1) # Azar

# list inside tuple --> we can use list operation 
fruit = ("azar",[1,2])
fruit[1].append(3)
print(fruit) # ('azar', [1, 2, 3])

# function 
# min, max, sum 
num = (1,5,9,3,2,7,87,657)
print(min(num)) # 1
print(max(num)) # 657
print(sum(num)) # 771

# Function retruning two values 
def get_re(n1, n2):
    add = n1+n2
    mul = n1*n2

    return add,mul

add, mul = get_re(3,4)
print(add)
print(mul)
'''

# more about tuples 

num = tuple(range(1,10))
print(num) # (1, 2, 3, 4, 5, 6, 7, 8, 9)

num1 = list(num)
print(num1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(type(num)) # <class 'tuple'>
print(type(num1)) # <class 'list'>

# tuple, list to string 

numtup = str(num)
numlis = str(num1)

print(type(numtup)) # <class 'str'>
print(type(numlis)) # <class 'str'>
