# what is list comprehension
# using loop  we can create list in one line

# Example
# create a list of square from 1 to 10

# simple method

from ast import comprehension

from numpy import append, var


square = []
for i in range(1, 11):
    square.append(i**2)
print(square)

# list comprehension

square1 = [i**2 for i in range(1, 11)]
print(square1)

# negative number
# simple method
neg = []
for i in range(1, 11):
    neg.append(-i)
print(neg)
# list comprehension

neg1 = [-i for i in range(1, 11)]
print(neg1)

# display starting letter

# simple method
start_letter = []
names = ["azar", "udeen", "shariff"]
for name in names:
    start_letter.append(name[0])
print(start_letter)

# list comprehension
names = ["azar", "udeen", "shariff"]
start_letter1 = [name[0] for name in names]
print(start_letter1)

# take a list of names and reverse them in the list using list comprehension and function
name_list = ["azar", "udeen", "shariff"]
rev_name = []
for name in name_list:
    rev_name.append(name[::-1])
print(rev_name)

# list comprehension


def rev_na(name_list):
    rev_name1 = [name[::-1] for name in name_list]
    return rev_name1


print(rev_na(names))

# list comprehension with if statement

# even or odd

# simple method

num = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for i in num:
    if (i % 2 == 0):
        even.append(i)
print(even)

# list comprehension
even = [i for i in num if (i % 2 == 0)]
print(even)

# num to string

var_list = [True, False, [1, 2, 3], 1, 1.2, 3]

store = [str(i) for i in var_list if(type(i) == int or type(i)==float)  ]

print(store)

# new_var=[]

# for i in var_list:
#     if(type(i) == int or type(i)== float):
#         new_var.append(i)
# print(new_var)


# list comprehension with if else 

# syntax: [append if else for ]

num = [1,2,3,4,5,6,7,8,9,10]

new_na = [i if i%2==0 else -i for i in num]

print(new_na)


# list comprehension using nested list (list inside list)

# [[1,2,3],[1,2,3],[1,2,3]]

list_list = []

for i in range(3):
    list_list.append(list(range(1,4)))

print(list_list)

# list comprehension 

list_new = [[1,2,3] for i in range(3)]
print(list_new)