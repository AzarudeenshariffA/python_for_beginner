'''
# keyword arguments and store as dictionary 
# **kwargs (double star operator)

# dictionary 
# kwargs as a parameter

def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

d = {"name":"azar","age":20}

func(**d)
"""name:azar
age:20"""
# function with all type of parameter 
# important to understand
# PADK
# we mostly use two
"""parameter, *args, default parameter="unknown", **kwargs"""
def func_print(*args,age="None",**kwargs):

    print(args)
    print(age)
    print(kwargs)
func_print(1,2,3,name="azar",age1=20)
# {'name': 'azar', 'age1': 20}

# make a func
def is_rev(*args,**kwargs):
    emp = []
    if kwargs.get("rev") == True:
        for i in args:
            emp.append(i[::-1])
        return emp
    else:
        return args

name = ["azar","uddin"]
print(is_rev(*name,rev = True))
# ['raza', 'niddu']
'''