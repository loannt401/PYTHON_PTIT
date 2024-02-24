import math

def snt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

lst = [int(x) for x in input().split()]
n = lst[0]
m = lst[1]
a = []
t = n
while t>0:
    t-=1
    x = [int(x) for x in input().split()]
    a.append(x)

for i in range(n):
    for j in range(m):
        if snt(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0

for i in range(n):
    s = ""
    for j in range(m):
        s += str(a[i][j]) + " "
    print(s)
    s = ""

        

'''

3 3
1 2 3
4 5 6
7 8 9

'''