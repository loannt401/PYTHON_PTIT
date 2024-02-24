




t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    dict = {}
    for v in a:
        if v in dict:
            dict[v] = dict[v] + 1
        else:
            dict[v] = 1

    ok = False 
    for v in dict:
        if dict[v] > n//2:
            print(v)
            ok = True

    if ok == False:
        print("NO")


'''

2
9
3 3 4 2 4 4 2 4 4
8
3 3 4 2 4 4 2 4

'''


