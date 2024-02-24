
t = int(input())
while t>0:
    t-=1
    lst = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    idx1, idx2, idx3, ok = 0,0,0,0
    while idx1<lst[0] and idx2<lst[1] and idx3<lst[2]:
        if a[idx1] == b[idx2] and b[idx2] == c[idx3]:
            print(a[idx1], end=" ")
            idx1 += 1
            idx2 += 1
            idx3 += 1
            ok = 1
        elif a[idx1] < b[idx2]:
            idx1 += 1
        elif b[idx2] < c[idx3]:
            idx2 += 1
        elif c[idx3] < a[idx1]:
            idx3 += 1
    if ok == 0:
        print("NO")
    else:
        print()





    
    
    
    

    



'''

3
6 5 8
1 5 10 20 40 80
5 7 20 80 100
3 4 15 20 30 70 80 120
3 5 4
1 5 5
3 4 5 5 10
5 5 10 20
3 3 3
1 2 3
4 5 6
7 8 9

'''