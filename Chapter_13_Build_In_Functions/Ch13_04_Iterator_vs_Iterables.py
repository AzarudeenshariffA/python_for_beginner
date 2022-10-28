# string , tuples are iterables
# map function return iterator 

# how a loop works 
'''
step 1 : call iter function 
step 2 : iter(num) return iterator 
step 3: next(iter(num))
'''
# for example 
num = [1,2,3,4,5,6,7,8]

num_iter = iter(num)
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))

# 1
# 2
# 3
# 4

# iterators 
# map and filter function gives iterator so we can just call next func 

# print(list(filter(lambda a:a%2==0 , list(range(1,11)))))
eve_iter = filter(lambda a:a%2==0 , list(range(1,11)))
print(next(eve_iter))
print(next(eve_iter))
print(next(eve_iter))
print(next(eve_iter))
print(next(eve_iter))
# 2
# 4
# 6
# 8
# 10