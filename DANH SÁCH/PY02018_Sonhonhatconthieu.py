
n = int(input())
a = [int(x) for x in input().split()]
check = [0*x for x in range(30000)]
for v in a:
    check[v] += 1
for i in range(1,len(check)):
    if check[i] == 0:
        print(i)
        break

    
        


'''

3
1 2 4

'''