# string slicing

language = "Python"
# p  y  t  h  o  n
# 0  1  2  3  4  5
#-6 -5 -4 -3 -2 -1

# position(index number)-->positive,negative

print(language[2])  # t

print(language[-1])  # n


# String slicing
language = "Python"

print(language[:])  # Python


print(language[2:5])  # tho

# Step Arguments

print(language[::-1])  # nohtyP (start,end-1,step)

print(language[::3])  # Ph

# Excercise 3
"""ask user name and print backward name in reverse order make your program in two lines"""

# ans
name = input("Enter Your name: ")
print(name[::-1])
