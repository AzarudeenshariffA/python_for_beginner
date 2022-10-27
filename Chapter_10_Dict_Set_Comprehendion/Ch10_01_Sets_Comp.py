# mostly we dont use 
# unordered 

set1 = {i**2 for i in range(1,11)}
print(set1) # {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
# names start

name = {"azar","az","uddin"}

name_c = {i[0] for i in name }
print(name_c) # {'u', 'a'}