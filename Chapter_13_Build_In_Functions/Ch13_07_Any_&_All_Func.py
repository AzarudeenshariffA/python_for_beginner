'''
# any and all function --> retrun true or false 
# all --> if all true means then all function return true 
# any --> if any one true means then any one function return true 

num1 = [2,4,6,8,10]

num2 = [1,3,5,7,9]

all_chk = all([i%2==0 for i in num1]) 
any_chk = any([i%2==0 for i in num2]) 

print(all_chk) # True
print(any_chk) # False
'''
# check the given tuple consist of int and float 

def find_dt(args):
    df = all([type(arg)==int or type(arg)== float for arg in args])
    return df

list_m=(1,2,3,"a")
print(find_dt(list_m))