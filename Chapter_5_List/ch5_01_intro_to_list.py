# List is a Data structure
# ordered collection of items
# we can store anything in lists int,float,string
# list is created using []

# example 
list1 = [1, 2, 'hi', 6.8, None]
print(list1) # [1, 2, 'hi', 6.8, None]

# Accessing position of list 
list1 = [1, 2, 'hi', 6.8, None]
print(list1[2]) # hi
print(list1[:3]) # [1, 2, 'hi']

# To Change Data in list 

mix = [1,2,3]
mix[1]="two"
print(mix) # [1, 'two', 3]

mix[1:] = 'two'
print(mix) #[1, 't', 'w', 'o']

mix[1:]=['two','three']
print(mix) # [1, 'two', 'three']


# Add data to list
# Append method --> append at last

num = [1,4,3]
num.append(5)
print(num) 

# more methods to add data in a list 

# Insert method
num = [1,4,3]
num.insert(1,2)
print(num) # [1, 2, 4, 3]

# extend method  
from distutils.command.build_scripts import first_line_re


fruits1 = [1,2,3]
fruits2 = [4,5,6]

fruits1.extend(fruits2)
fruits1.append(fruits2)
print(fruits1) # [1, 2, 3, [4, 5, 6]]
print(fruits1) # [1, 2, 3, 4, 5, 6]

# Delete data from list 
# pop method (pop method will return the popped value)
from ast import keyword


fruits1 = [1,2,3]
fruits1.pop()
print(fruits1) # [1, 2]

# del keyword
del fruits1
print(fruits1) # error

# remove method 
fruits1 = [1,2,3]
fruits1.remove(2)
print(fruits1) # [1, 3]

# in keyword in list 
list1 = ["azar","apple","banana"]

if "azar" in list1:
    print("yes")
else:
    print("no")

# some more methods in list 

fruits = ['apple','orange','grapes','mango']

# count
# sort method 
# sorted function 
# reverse 
# clear 
# copy 

print(fruits.count('apple')) # 1

fruits.sort()
print(fruits) # ['apple', 'grapes', 'mango', 'orange']

number = [4,2,1,6,9,7]

# sorted function 
print(sorted(number)) # [1, 2, 4, 6, 7, 9]

# empty 
number.clear()
print(number) # []

# copy 
num1 = number.copy()
print(num1) # []

# is vs equal 

fruit = [1,2,3]
fruit1 = [1,2,3]
print(fruit == fruit1) # true
print(fruit is fruit1) # false

fruit = [1,2,3]
fruit1 = fruit.copy()
print(fruit is fruit1) # check our list present in same location or not # false

fruit = [1,2,3]
fruit1 = fruit
print(fruit is fruit1) # true

# join and split method 

# split method --> convert string to list 
user = "azar 21".split()
print(user) # ['azar', '21']

user = ['azar', '21'] # 21 need to be in string then only it concatenate
print('#'.join(user)) # azar#21
# join method --> convert list to string 
# List vs Array  --> order collection of item in python
# list --> collection of different datatypes
# array --> collection of similar datatypes (we use numpy array)

# List vs String 
# string are immutable --> we cant change original string 
# list are mutable --> we can change original list 


# Loop in List 

fruits = ['orange', 'apple', 'mango', 'banana'] # use for loop in list

# for fruit in fruits:
#     print(fruit)

# i = 0
# while(i<len(fruits)):
#     print(fruits[i])
#     i+=1

# list inside list 

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# list inside a list is know as 2d array 
print(matrix[2][1]) # 8

# type function 

print(type(matrix)) # list 

# more about list 

# range function 

num = list(range(1,10))
print(num) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# pop method 
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
popped = num.pop()
print(popped)

# pass list in a function 

def neg_num(n):
    num = list(range(-1,(-1*n)-1,-1))
    print(num)
neg_num(10)


# min and max function 
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(min(num)) # 1
print(max(num)) # 9