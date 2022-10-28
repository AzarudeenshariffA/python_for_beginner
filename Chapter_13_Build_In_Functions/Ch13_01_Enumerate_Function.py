# enumerate function
# we use with for loop to track position of our item is iterable 
# when we use for loop with tuple and list we track item not position 

# simple method 
name = ["abc", "abcdef"]

pos = 0
for i in name:
    print(f"{pos}--> {i}")
    pos=pos+1

# 0--> abc
# 1--> abcdef

# with enumerate 
name = ["abc", "abcdef"]

for pos,item in enumerate(name):
    print(f"{pos}--> {item}")
'''0--> abc
1--> abcdef'''

# problem 
'''define a function that take two arguement
1) list containing string 
2) string that want to find in your list and this function will return the index of string in your list and if string is not present retrun -1
'''
def find_pos(list_name, target_name):
    for pos, item in enumerate(list_name):
        if item==target_name:
            return pos 
    else:
        return -1
name = ["azar",'udeen',"shariff"]
print(find_pos(name,"uddin")) # -1

