
t = int(input())

while t>0:
    t-=1
    n = int(input())
    s = input()
    sl = len(s)
    a = []
    r = l = 0

    # tach xau ra thanh tung nhom nho hon 1e3
    while sl >= int(1e3):
        r = l + int(1e3)
        while s[r] != ' ':
            r -= 1
        x = s[l:r]
        a.append(x)
        l = r
        sl -= len(x)
    
    if sl > 0:
        a.append(s[l:])

    min1 = min2 = min3 = int(1e8)

    for v in a:
        tmp = [int(x) for x in v.split()]
        if min(tmp) < min1:
            min3 = min2
            min2 = min1
            min1 = min(tmp)
            tmp.remove(min1)
        if min(tmp) < min2:
            min3 = min2
            min2 = min(tmp)
            tmp.remove(min2)
        if min(tmp) < min3:
            min3 = min(tmp)
            tmp.remove(min3)
        del tmp
    
    print(min1+min2+min3)


'''

2
7
1 2 3 0 -1 8 10 
7
9 8 20 3 4 -1 0

'''