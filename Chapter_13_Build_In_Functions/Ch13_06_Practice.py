# [1,2,3],[4,5,6],[7,8,9] return average 

# simple method 

list_num = [[1,2,3],[4,5,6],[7,8,9]]
new_list = []
for i in list_num:
    temp = 0
    for j in i:
        temp = temp + j
    temp = temp / 3
    new_list.append(int(temp))
print(new_list) # [2, 5, 8]


# another method --> 1+4+7
av =[]
def avg(list_num):
    for pair in zip(*list_num):
        av.append(sum(pair)/len(pair))
        print(av)
avg(list_num)


