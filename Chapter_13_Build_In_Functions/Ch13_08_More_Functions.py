'''
# advance min and max 

# print the highest len string from the list 

def print_max(n):
    print(max(n, key=lambda a: len(a)))

print_max(["Azarudeen","azr","azar"]) # Azarudeen

# print the max age 

student = {
    "azar" : {"Score":50,"age":24},
    "azarud" : {"Score":60,"age":34}
}

print(max(student, key=lambda a:student[a]["age"])) # Azaru

# Advance sorted function 
#  sort function --> sort method is not available in tupes
fruits = ["grapes","orange","apple"]
fruits.sort()
print(fruits) # ['apple', 'grapes', 'orange']

# to sort tupes we use sorted functions 
# tuples are immutable 
fruit = ("grapes","orange","apple")
print(sorted(fruit))  # ['apple', 'grapes', 'orange']

# sets 
fruit_S = {"grapes","orange","apple"}
print(sorted(fruit_S))  # ['apple', 'grapes', 'orange']
'''

# dict 
student = [
     {"Score":50,"age":54},
    {"Score":60,"age":34}
]
print(sorted(student,key=lambda a:a["age"])) # [{'Score': 60, 'age': 34}, {'Score': 50, 'age': 54}]

# more about func 

# what are doc strings --> to see what  a func do
# how to write doc string --> '''''' or """"""
# how to see docstrings  --> print(add.__doc___)

# example 
def add(a,b):
    '''this func take two input and perfom addition'''
    return (a+b)

print(add(4,5)) # 9
print(add.__doc__) # this func take two input and perfom addition

# if you want to know what a func does 
print(help(list))