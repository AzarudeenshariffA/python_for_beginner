# strings --> collection of characters inside single or double qoutes


# STRINGS ARE IMMUTABLE --> WE CAN'T CHANGE ORIGINAL STRING (string methods will not change original string or character of string) but we can change value of a variable

# string concatenation

first_name = "azar"

last_name = "uddin"

print(first_name+" "+last_name)

"""we can't concatenate string with different data types
but we can do it with the help of type casting
"""
first_name = "azar"
num = 10
print(first_name+" "+str(num))
print((first_name+" ")*num)

# User Input --> input  function (gets input in form of strings)

name = input("enter your name: ")

print(name)

# type casting(string to int)
# whole num is know as integer

num1 = int(input("enter num1 : "))  # string to int
num2 = float(input("enter num2 : "))  # string to float
print(num1+num2)  # ans will in float


# more about variable

num1, num2 = 24, 25

print(num1+num2)

x = y = z = 1

print(x+y+z)

# split function

name = "azar uddin"

print(name.split())


# two or more input in one line using split function

num1, num2 = input("Enter two numbers ").split()

print(int(num1)+int(num2))

# String Formattting
name = "Azar"
age = 18

print("my name is "+name+" and my age is "+str(age))
print("my name is {} and my age is {}".format(name, age))
print(f"my name is {name} and my age is {age}")


# Excersise 2
"""ask user to input 3 numbers and you have to print their avg """

# ans
num1, num2, num3 = input(
    "Enter three marks separated with commas: ").split(",")
print((int(num1)+int(num2)+int(num3))/3)  # retruns in float
