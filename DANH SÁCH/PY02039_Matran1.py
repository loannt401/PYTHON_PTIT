n = int(input())
a = []
for i in range(n):
    v = [int(x) for x in input().split()]
    a.append(v)
k = int(input())

tongtren = 0
for i in range(n):
    for j in range(i+1,n):
        tongtren += a[i][j]

tongduoi = 0
for i in range(n):
    for j in range(i):
        tongduoi += a[i][j]

kq = abs(tongtren - tongduoi)
if kq <= k:
    print("YES")
else:
    print("NO")
print(kq)


'''

5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5

'''