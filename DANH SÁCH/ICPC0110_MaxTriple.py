
t = int(input())
while t>0:
    t-=1
    n = int(input())
    s = input()
    dai = len(s)
    a = []
    
    l=r=0
    while dai >= int(1e3):
        r = l + int(1e3)
        while s[r] != ' ':
            r-=1
        x = s[l:r]
        a.append(x)
        l=r
        dai -= len(x)
    
    if dai > 0:
        a.append(s[l:])

    max1 = max2 = max3 = int(-1e8)

    for v in a:
        tmp = [int(x) for x in v.split()]
        if max(tmp) > max1:
            max3 = max2
            max2 = max1
            max1 = max(tmp)
            tmp.remove(max1)
        if max(tmp) > max2:
            max3 = max2
            max2 = max(tmp)
            tmp.remove(max2)
        if max(tmp) > max3:
            max3 = max(tmp)
            tmp.remove(max3)
        del tmp
    
    print(max1 + max2 + max3)

'''

2
7
1 2 3 0 -1 8 10 
7
9 8 20 3 4 -1 0

'''