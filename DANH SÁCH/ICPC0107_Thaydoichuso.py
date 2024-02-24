

def soasangb(s,a,b):
    res = ""
    for c in s:
        if(c == a):
            res += b
        else:
            res += c
    return res

def sobsanga(s,a,b):
    res = ""
    for c in s:
        if(c == b):
            res += a
        else:
            res += c
    return res

t = int(input())

while t>0:
    t-=1
    lst = input().split()
    a = lst[0]
    b = lst[1]
    s = input()
    try:
        lst = s.split()
        s1 = lst[0]
        s2 = lst[1]  
    except:
        s1 = s
        s2 = input()

    so1 = int(soasangb(s1,a,b))
    so2 = int(sobsanga(s1,a,b))
    lon1 = so1 if so1 > so2 else so2
    nho1 = so1 if so1 < so2 else so2

    so3 = int(soasangb(s2,a,b))
    so4 = int(sobsanga(s2,a,b))
    lon2 = so3 if so3 > so4 else so4
    nho2 = so3 if so3 < so4 else so4
    print(nho1+nho2, lon1+lon2)

