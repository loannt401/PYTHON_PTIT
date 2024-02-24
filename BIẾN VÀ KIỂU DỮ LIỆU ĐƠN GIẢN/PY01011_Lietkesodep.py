


def sothuannghich(n):
    s = str(n)
    l=0
    r = len(s)-1
    while l<r:
        if s[l] != s[r] :
            return False
        l+=1
        r-=1
    return True

def ktso(n):
    s = str(n)
    for v in s:
        if int(v)%2==1:
            return False
    return True

def sochuso(n):
    s = str(n)
    if len(s) % 2 == 0: return True
    return False

t = int(input())
while t>0:
    t-=1
    lst = []
    n = int(input())
    for i in range(22,n,22):
        if sochuso(i):
            if ktso(i):
                if sothuannghich(i):
                    lst.append(i)
                    
    s = ""
    for v in lst:
        s += (str(v) + " ")
    print(s)
