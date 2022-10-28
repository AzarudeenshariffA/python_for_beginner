# map is iterator
# we pass function in map 


# simple method 
def sqaure(a):
    return a**2

number=[1,2,3,4,5]
sq = list(map(sqaure,number))
print(sq) # [1, 4, 9, 16, 25]

# using lambda 
number=[1,2,3,4,5]
sq = list(map(lambda a : a**2, number))
print(sq) # [1, 4, 9, 16, 25]

# print the len of string 
str_name = ["Azar","udeen","shariff"]
le = list(map(len, str_name))
print(le) # [4, 5, 7]
# we can run only one loop in map function 
for i in le:
    print(i)
'''4
5
7'''

