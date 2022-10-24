
# for loop

# for with range function

for i in range(10): # i--> 0 to 9
    print("hello") # print 10 times hello

for i in range(1,10): # i--> 1 to 9(start to end-1)
    print(i) # print 1 to 9
# STEP ARGUEMENT

for i in range(1,10,2):
    print(i)
# o/p 
1
3
5
7
9
for i in range(10,-1,-1):
    print(i)
# o/p 
10
9
8
7
6
5
4
3
2
1
0

for i in range(-1,-11,-1):
    print(i)
# o/p 
-2
-3
-4
-5
-6
-7
-8
-9
-10

# example
# sum of numbers
n = 10
sum = 0
for i in range(1,11):
    sum+=i
print(sum)
# count char in name 

name = "azarudeen shariff"
temp_var= ""

for i in range (len(name)):
    if name[i] not in temp_var:
        temp_var=temp_var+name[i]
        print(f"{name[i]}: {name.count(name[i])}")
    i=i+1

print(temp_var)

# BREAK & CONTINUE keyword
# continue --> use to skip the loop
for i in range(10):
    if(i==5):
        continue
    print(i)
# o/p 
1
2
3
4
6
7
8
9

# break --> used to break the loop

for i in range(10):
    if(i==5):
        break
    print(i)
# o/p 
0
1
2
3
4


# for with strings

name = "azar"

for i in name:
    print(i)

# o/p 
# a
# z
# a
# r
