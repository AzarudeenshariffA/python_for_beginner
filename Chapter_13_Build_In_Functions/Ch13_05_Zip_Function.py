# it is a iterator
# zip --> merge


# example
user = ["user1", "user2", "user3"]
name = ["azar", "udeen", "shariff"]
lname = ["1","2","3"]

dict_zip = list(zip((user,name)))
print(dict_zip)
# [(['user1', 'user2', 'user3'],), (['azar', 'udeen', 'shariff'],)]

dict_zip1 = list(zip((*user,*name)))
print(dict_zip1)
# [('user1',), ('user2',), ('user3',), ('azar',), ('udeen',), ('shariff',)]

zip1 = list(zip((user,name,lname)))
print(zip1)

l1 = [1,3,5,7]
l2 = [2,4,6,8]


l = [(1,2),(3,4),(5,6),(7,8)]
print(list(zip(*l))) # [(1, 3, 5, 7), (2, 4, 6, 8)]

# reversing 
l1 , l2 = list(zip(*l))
print(l1[::-1])
print(l2[::-1])
# (7, 5, 3, 1)
# (8, 6, 4, 2)

em = []
for pair in zip(l1,l2): # pair --> seeing max(1,2)
    em.append(max(pair))
print(em) # [2, 4, 6, 8]