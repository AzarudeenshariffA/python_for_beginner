# we use dictionary to overcome limitation of list,tuple and they are not enough to represent real data 

# dictionary 
# is a key value pair 
# is a unordered collection of data 
# there is no indexing in dictionary
# duplicate key should not be used
'''
# Example
user={}
print(type(user)) # <class 'dict'>

# method 1 to create dict 
user = {"name":"azar", "age":21}
print(user) # {'name': 'azar', 'age': 21}

# method 2 to create dict 
user1 = dict(name = "azar", age = 18) 
print(user1) # {'name': 'azar', 'age': 18}

# to access data from dict 
user = {"name":"azar", "age":21}
print(user["name"]) # azar
print(user.keys()) # dict_keys(['name', 'age'])
print(user.values()) # dict_values(['azar', 21]) (but this are not list, we cant add or delete but we can iterate)
print(user.items()) # dict_items([('name', 'azar'), ('age', 21)])

# we can store any data in dict 
user_info={
    "name" : "azar",
    "degree" : ["be", "cse"],
    "skills" : ["python", "c", "c++"]
}

print(user_info["degree"])  # ['be', 'cse']


# looping and keywords in dictionary 
user_info={
    "name" : "azar",
    "degree" : ["be", "cse"],
    "skills" : ["python", "c", "c++"]
}

# check if key exist in dict or not 

if 'name' in user_info:
    print("present") # present

# loop in dict 

for i in user_info:
    print(i) 

# name
# degree
# skills

# item method 
user_info={
    "name" : "azar",
    "degree" : ["be", "cse"],
    "skills" : ["python", "c", "c++"]
}
for key, value in user_info.items():
    print(f"the key is {key} and the value is {value}")

# o/p 
"""
the key is name and the value is azar
the key is degree and the value is ['be', 'cse']
the key is skills and the value is ['python', 'c', 'c++']
"""
# pop method 
user_info={
    "name" : "azar",
    "degree" : ["be", "cse"],
    "skills" : ["python", "c", "c++"]
}

# popped = user_info.pop("name")
# print(popped) # azar 

# pop random item 
popped = user_info.popitem()
print(popped) # ('skills', ['python', 'c', 'c++'])

# update dictionary 
user_info={
    "name" : "azar",
    "degree" : ["be", "cse"],
    "skills" : ["python", "c", "c++"]
}

education = {"clg_Deg":"BE"}
user_info.update(education) 
print(user_info)# {'name': 'azar', 'degree': ['be', 'cse'], 'skills': ['python', 'c', 'c++'], 'clg_Deg': 'BE'}


# fromkeys method --> to create dictionary eg:different key same values

d= dict.fromkeys(["name","age"],"one")
print(d) # {'name': 'one', 'age': 'one'}

d = dict.fromkeys(range(1,10),"one")
print(d) # {1: 'one', 2: 'one', 3: 'one', 4: 'one', 5: 'one', 6: 'one', 7: 'one', 8: 'one', 9: 'one'}

# get method --> to handle error which the key is not presented in dictionary 

user_info = {"age":19}
print(user_info.get("name")) # None

# clear method 
user_info = {"age":19}
user_info.clear()
print(user_info) # {}

# copy method 

user_info = {"age":19}
user = user_info.copy()
print(user) # {'age': 19}

'''
# more about get method 
user_info = {"age":19}
print(user_info.get("name","not found")) # not found