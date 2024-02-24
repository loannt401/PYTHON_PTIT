

t = int(input())

while t>0:
    t-=1
    lst = list(input())
    idx = 0
    for i in range(1, len(lst)):
        if lst[i] <= lst[i-1]:
            idx = i-1
            break
    if idx == 0: print("NO")
    else:
        ok = True
        for i in range(idx, len(lst)-1):
            if lst[i] <= lst[i+1]:
                ok = False
                break
        if ok: print("YES")
        else: print("NO")