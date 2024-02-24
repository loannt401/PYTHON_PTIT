

t = int(input())
while t>0:
    t-=1
    n = int(input())
    F = [0*x for x in range(1001)]
    while n>0:
        n-=1
        x = int(input())
        F[x] += 1
    
    idx = max(F)
    a = []
    for i in range(1001):
        if F[i] == idx:
            a.append(i)
    a.sort()
    print(a[0])

'''

3
3
999
999
19
4
13
333
333
13
3
11
12
13

'''


