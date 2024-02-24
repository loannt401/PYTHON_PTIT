t = int(input())
while t>0:
    t-=1
    n = int(input())
    ok = False
    for i in range(1000):
        if n%7==0: 
            ok = True
            break
        lst = list(str(n))
        lst.reverse()
        m = int("".join(lst))
        n = n+m

    if ok:
        print(n)
    else:
        print(-1)