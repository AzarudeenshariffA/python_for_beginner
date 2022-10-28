# make flexible functoins 
# * operator 
# * args --> takes as tuple
# multiple input takes and store in tuple 


# for example 
def add_arr(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(add_arr(1,2,3,4,5))
# 15

# *args with normal parameter 
# syntax def num(normal parameter, *args)
def mul_num(num, *args):
    sum = []
    for i in args:
        sum.append(num*i)
    return sum

print(mul_num(8,2,3,4,5))
# [16, 24, 32, 40]

# args as argument --> we use to unpack arguements

def mul_ar(*args):
    mul = 1
    for i in args:
        mul = mul * i
    return mul

num_list = [1,2,3,4,5,6]
print(mul_ar(*num_list))
# 720

# list comprehensiond
def powerofthree(*args):
    power = []
    for i in args:
        power.append(i**3)
    return power
# [27, 64, 125, 216, 343]


num =  (3,4,5,6,7)
print(powerofthree(*num))


