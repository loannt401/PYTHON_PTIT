
lst = {1:1}

while True:
    x = []
    ok = False
    for v in lst:
        if v < 10**18:
            if v*2 not in lst:
                x.append(v*2)
            if v*3 not in lst:
                x.append(v*3)
            if v*5 not in lst:
                x.append(v*5)
    for v in x:
        lst[v] = 1
        ok = True
    if ok == False:
        break

a = sorted(lst)

dic = {}
p = 1
for v in a:
    dic[v] = p
    p+=1

t = int(input())
for i in range(t):
    n = int(input())
    if n in dic:
        print(dic[n])
    else:
        print("Not in sequence")
    
    
    
    

    



'''

11
1
2
6
7
8
9
10
11
12
13
14

'''