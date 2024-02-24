
t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    dic = {}
    for v in a:
        if v not in dic:
            dic[v] = 1
        else:
            dic[v] += 1
    for v in dic:
        if dic[v] % 2 == 1:
            print(v)
            break


'''

2
7
1 2 3 2 3 1 3
5
1 1 3 3 2

'''