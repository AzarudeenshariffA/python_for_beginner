# dictionary comprehension same as dict 

# square = {1:1,2:4,3:9}

from ast import comprehension

from numpy import square


sq = {}
for i in range(1,4):
    sq[i]=i*i

print(sq)

# dict comprehension 

sq1 = {i:i*i for i in range(1,4)} # key value
print(sq1)

# another way

square={f"square of {num} is" : num**2 for num in range(1,11)}

for k,v in square.items():
    print(f"{k}:{v}")

# counting words 

st = "azarudeenshariff"
w_c = {}
for i in st:
    w_c[i] = st.count(i)

print(w_c)

# list_comprenhension 

st1 = {i:st.count(i) for i in st}
print(st1)

# D C with if else 

d = {1:'odd',2:'even'}

em = {}

for i in range(1,11):
    if(i%2==0):
        em[i]="even"
    else:
        em[i]="odd"
print(em)

# list comprehension 

em1 = {i:"even" if i%2==0 else "odd" for i in range(1,11)}
print(em1)