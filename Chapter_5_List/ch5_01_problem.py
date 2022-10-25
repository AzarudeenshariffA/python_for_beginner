
# square of number in list  
def square_num(n):
    list = []
    for i in n:
        m=i*i
        list.append(m)
    print(list)
num = [1,2,3,4]
square_num(num) # [1, 4, 9, 16]

# reverse list 
def reverse(n):
    print(n[::-1])
num = [1,2,3,4]
reverse(num)

# reverse 2d list 
def rev_list(n):
    ele = []
    for i in n:
        ele.append(i[::-1])
    print(ele)
num=[[1,2,3],[4,5,6],[7,8,9]]
rev_list(num)

# filer odd even 

def odd_even(n):
    odd=[]
    even=[]
    for i in n:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print([odd,even])
num = [1,2,3,4,5,6,7,8,9,10]
odd_even(num)

# union 
num1 = [1,2,3]
num2 = [1,2,4]

def union(n,n1):
    ele = []
    for i in n:
        if(i in n1):
            ele.append(i)
    print(ele)
union(num1,num2) # [1, 2]

# greatest difference 

num = [1,2,78] 

def great_dif(n):
    df = max(n) - min(n)
    # print(df)
    return df

print(great_dif(num))


# no of sublist in list 

num = [1,2,3,[1,2],[4,5]]

def count_sub_list(n):
    count = 0
    for i in n:
        if(type(i)==list):
            count+=1
    return count

print(count_sub_list(num)) # 2