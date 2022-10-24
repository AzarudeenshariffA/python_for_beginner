
'''
language = "Python"
# p  y  t  h  o  n
# 0  1  2  3  4  5
#-6 -5 -4 -3 -2 -1 

#len function return length of the string

print(len(language)) # 6

# lower and upper method

print(language.lower()) # python
print(language.upper()) # PYTHON

# title method --> makes starting letter capital

print(language.title()) # Python

# count method

print(language.count('o')) # 1

# problem
"""take two comma separated inputs from user (name and a single character) and print the length and character count in the name and also case insenstive count"""

name , char = input("enter your name and char: ").split(",")

print(f"the length of the name is {len(name)} and the char count in the name is {name.count(char)}")

# strip method

name =" azar  "
dots= ".............."
print(name+dots)
#to remove space from left
print(name.lstrip()+dots)
#to remove space from right
print(name.rstrip())
#to remove space from left and right
print(name.strip())
# o/p
"""
 azar  ..............
azar  ..............
 azar
azar
"""

# replace method
name = "azar"

print(name.replace("a","r"))

# exercise 4

name = "azar    ,  a"
name1, char = name.split(",")
print(f"name len is {len(name1.strip())} and count is {name1.count(char.strip())}")

# find and replace method

# replace method

string = "she is beautifull?"

print(string.replace("?","!")) #oldword,newword,how letter need to replace
print(string.replace("e","a",1))

# find() method

print(string.find("?")) #find, how how many letter after need to find #17
print(string.find("e",3))

# center method

name = "azar"
print(name.center(11,"*")) #****azar*** (11)

'''

# problem

name = input("enter your name ")
le = len(name)
print(f"hi {name.center(le+8,'$')}")  # hi $$$$azar$$$$
