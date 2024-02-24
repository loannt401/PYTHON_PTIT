


max_val = int(1e5)
X = []

def daydocdac(a,b):
    lst = []
    for i in range(a, b+1):
        if len(lst) == 0: lst.append(X[i])
        else:
            if X[i] in lst:
                lst.remove(X[i])
            else :
                lst.append(X[i])

    if len(lst) > 0: return True
    return False
    

t = int(input())
while t>0:
    t-=1
    n = int(input())
    s = input().split()
    for v in s:
        X.append(int(v))

    ok = True
    for i in range(n-1):
        for j in range(i+1,n):
            if not daydocdac(i,j): 
                ok = False
                break

    if ok: 
        print("YES")
    else:
        print("NO") 
    
    X.clear()





        