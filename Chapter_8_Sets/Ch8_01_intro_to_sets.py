# set datatypes 
# unordered collection of unique items 
# no item should be displayed 
# set mainly used to remove duplicate items
# we store str,int,float but we can't store list, tuple, dictionary 

# creating a set 
s={1,2,3,3}
print(type(s)) # <class 'set'>
print(s) # {1,2,3}
# set methods 

# add method 
s = {1,2,3,4}
s.add(6)
s.add(7)
print(s) # {1, 2, 3, 4, 6, 7}

# remove method 
s.remove(2)
print(s) # {1, 3, 4, 6, 7}

# discard method (it is like remove method , if item is not present means it will not throw )
s.discard(1)
print(s) # {3, 4, 6, 7}

# copy method 
s1= s.copy()
print(s1) # {3, 4, 6, 7}

# clear method
s.clear()
print(s) # set()

# more about sets 
# we can use in keyword in sets
s = {1,2,3,4,5}

if 1 in s:
    print("yes") # yes

for i in s:
    print(i)


# set maths 
s1={1,2,3,4}
s2={1,2,3,4,5}

# operation in sets(union | , intersection & )

# union operation 
union_Set = s1 | s2 
print(union_Set) # {1, 2, 3, 4, 5}

# intersection operation 
intersection_Set = s1 & s2 
print(intersection_Set) # {1, 2, 3, 4}


