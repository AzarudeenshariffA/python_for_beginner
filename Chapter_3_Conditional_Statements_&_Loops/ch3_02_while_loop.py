
# while loop

# print hello 10 times

i=1 #initiaxling 1
while i<=10: # checks the condition if true then it enters or if false then it will exit out of loop
    print("hello")
    i=i+1 # increamenting

# sum of n numbers
n = 10
i = 1
sum = 0
while(i<=n):
    sum = sum + i
    i=i+1
print(sum)

# calculate the number 1257 as 1+2+5+7

num = 1257
sum = 0
while num!=0:
    digit = num%10
    sum = sum+digit
    num = num//10
print(sum)


# count char in name 

name = "azarudeen shariff"
temp_var= ""

i = 0
while(i<len(name)):
    if name[i] not in temp_var:
        temp_var=temp_var+name[i]
        print(f"{name[i]}: {name.count(name[i])}")
    i=i+1

print(temp_var)


# infinte loop (by knowing or by mistake)

# by knowing
while(True):
    print("hello")

# by mistake
i=0
while(i<10):
    print("hello")
