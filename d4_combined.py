dict1 = {'a':10,'b':20,'c':30}
dict2 = {'b':15,'c':5,'d':50}

dict3 = {}

dict3.update(dict1)
dict3.update(dict2)

for x,y in dict1.items():
    for a,b in dict2.items():
        if x == a:
            n = y + b
            dict3[x] = n 

print(dict3)
