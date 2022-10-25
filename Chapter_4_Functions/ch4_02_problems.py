# fibonacci series 
# 0 1 1 2 3 5 8 13 21 34 55

def fib(num):
    a = 0
    b = 1
    sum = 0
    if(num==1):
        return 1
    for i in range(1,num):
        sum=a+b
        a=b
        b=sum 
    return sum

print(fib(3))

# palindrome of three num
# it is bruteforce method, we can also do in pythonic way
def pal(num):
    temp = 100
    num1 = 0
    i = 1
    while(num!=0):
        dig = num%10 
        num1 = num1+int(dig*(10000/(10**i)))
        num = num//10
        i = i + 1
    print(num1)

pal(1234)



