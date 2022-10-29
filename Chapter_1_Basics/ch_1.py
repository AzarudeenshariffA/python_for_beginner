

#Print function
print("hello world")

#String--> collection of character inside single or double quotes

print("hello 'hi' world")

#Escape Sequence
print("\' \" ")  
print("\\")
print("line A\nline B ") #NEW LINE
print("line A\t line B") #NEW TAB
print("line A\bline B") #BACKSPACE
print("\\\\") 

#Comments--> interpreter will not reaa
#single line comment

#hello world

#multi line comment
 
"""
hello 
world
"""

#Excercise 1
"""
quetion (print below)
this is \\ double backslash
there are /\/\/\ mountains
he is    awesome
"""

#(ans)

print("this is \\\\ double backslash")
print("there are /\\/\\/\\ mountains")
print("he is \t awesome")
print("\\\" \\\n \\\t \\\' ")

#Raw Strings--> escape sequence will treat as normal strings

print(r"line A\nline B ")

#print emoji

print("\u0003")
#O/P ♥

#Python as calculator 

#operators --> +,-,*,/,%(exponent--> remainder),**

print(2**0.5) #0.5 will become root

print(2**2) #becames 2power2

# Assignment operators

num = 1
num+=1
print(num) #2

# boolean operator
# And, or--> see in chapter 3 folder

#To calculate big number python uses precedence rule 
"""
remember parenthesis() to calculate big number --> highest
exponent --> r to l
*,/(float devision),//(integer devision),% --> l to r
+,- --> l to r
"""

#variable in python
"""
a=2 we are assigning value 

we can change variable

we can store string and number

"""
#assigning variable rules
"""
we can't write a variable name start as number 
we can use alphabets and underscore in starting letter but not number or special symbol
eg:-$name='hi'
"""

#naming conventions--> 
#snakecase writing --> user_first_name 

#we use snakecase in python