
t = int(input())
while t > 0:
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    lst = []
    for i in range(n):
        while len(lst) > 0 and a[lst[-1]] <= a[i]:
            lst.pop()
        if len(lst) == 0:
            print(i+1, end = " ")
        else:
            print(i-lst[-1], end = " ")
        lst.append(i)
    print()


'''

1
7
100 80 60 70 60 75 85

'''