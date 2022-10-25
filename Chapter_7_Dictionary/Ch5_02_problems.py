# cube number 

def cube(num):
    cu = {}
    for i in range(1,num):
        cu[i] = i**3
    return cu

print(cube(5)) # {1: 1, 2: 8, 3: 27, 4: 64}

# word counter 

def word_counter(char):
    ch = {}
    for i in char:
        ch[i] = char.count(i)
    return ch

print(word_counter("azarudeen")) # {'a': 2, 'z': 1, 'r': 1, 'u': 1, 'd': 1, 'e': 2, 'n': 1}

user_info={
    "name" : "azar",
    "degree" : ["be", "cse"],
    "skills" : ["python", "c", "c++"]
}

# solution 

user_in ={}

user_in["name"] = "azar"
user_in["age"] = 19
user_in["degree"] = ["be", "cse"]
user_in["skills"] = ["python", "c", "c++"]
for key,value in user_in.items():
    print(f"{key}:{value}")
# o/p 
'''
name:azar
age:19
degree:['be', 'cse']
skills:['python', 'c', 'c++']
'''