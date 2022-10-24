
# Pass Statement --> if we don't need to write any code in statements

x = 18
if x>0:
    pass

# if condition
"""
Syntax
if(condition):
    statement
"""
age = 19
if age>18:
    print("he is above 18")

# if-else statement
age = 17
if age>18:
    print("age is above 18")
else:
    print("age is below 18")

# if-elif-else statement
age = 18
if age>18:
    print("age is above 18")
elif age==18:
    print("age is equal 18")
else:
    print("age is below 18")

# Nested if-else
guess_num = 24
user_num = 24
if user_num==guess_num:
    print("you won")
else:
    if user_num>guess_num:
        print("too high")
    else:
        print("too low")


# And, Or Operator --> check two condtion at same time

# and --> if both condition are true then only it becames true
# t+t=t
# t+f=f
# f+t=f
# f+f=f
name = "abcd"
age = 18
if name=="abcd" and age==18:
    print("true")
else:
    print("false")

# or --> if one condition is true then it becames true
# t+t=t
# t+f=t
# f+t=t
# f+f=f

name = "abcd"
age = 18
if name=="abcd" or age==19:
    print("true")
else:
    print("false")

# in keyword
name = "azar"
if 'a' in name:
    print("present!!!!!")

# check empty or not
name = "kol"

if name:
    print("value present in name")
else:
    print("value is not present in name")

# Excersice 1
"""if user name starts with a or A and age is above 18 then he can watch netflix"""
# ans
name = "Azar"
age = 19
if (name.lower())[0] == 'a' and age>18:
    print("you can watch netflix")
else:
    print("you can't watch")



