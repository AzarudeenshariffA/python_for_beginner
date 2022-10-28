# we can iterate only one time (or) we can run only one time a loop in map and filter object, if we 
# convert them in tuple, list we can run many loop 

#  we can iterate
# if the function return true then only it stores 

# simple method 

def is_eve(a):
    emp = []
    for i in a:
        if(i%2==0):
            emp.append(i)
    return emp 
print(is_eve([1,2,3,4,5,6,7,8,9,10]))
# [2, 4, 6, 8, 10]
# using filter method 

print(list(filter(lambda a:a%2==0 , list(range(1,11)))))
# [2, 4, 6, 8, 10]

# list comprehension 
num = list(range(1,13))
fil_even = [i for i in num if i%2==0 ]
print(fil_even)