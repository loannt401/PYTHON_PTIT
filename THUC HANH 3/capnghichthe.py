
n = int(input())
lst = input().split()
lst1 = []
for i in lst:
    lst1.append(int(i))

dem = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        if lst1[i] > lst1[j]:
            dem += 1


print(dem)

