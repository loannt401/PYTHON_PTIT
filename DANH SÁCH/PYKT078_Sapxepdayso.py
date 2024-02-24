
t = int(input())
while t>0:
    t-=1
    lst = [int(x) for x in input().split()]
    n = lst[0]
    m = lst[1]
    a = [int(x) for x in input().split()]
    ma = max(a)
    idx = -1
    for i in range(n):
        if a[i] == ma:
            idx = i
            break
    a.append(0)
    i = n
    while i > idx:
        a[i] = a[i-1]
        i -= 1
    a[i] = m

    for v in a:
        if v<0:
            print(v, end = " ")
    
    for v in a:
        if v >= 0:
            print(v, end = " ")
    print()




'''

1
5 3
-1 2 3 4 -1

'''