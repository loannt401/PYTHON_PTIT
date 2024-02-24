
t = int(input())
while t>0:
    t-=1
    n = int(input())
    F = [0*x for x in range(1001)]
    a = [int(x) for x in input().split()]
    ma = max(a)
    mi = min(a)
    for v in a:
        F[v] += 1
    dem = 0
    for i in range(mi, ma+1):
        if F[i] == 0: 
            dem += 1
    print(dem)





'''

2
5
4 5 3 8 6
3
2 1 3

'''