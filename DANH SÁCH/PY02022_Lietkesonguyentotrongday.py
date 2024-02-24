import math

def snt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

n = int(input())
arr = [int(x) for x in input().split()]
dic = {}
a = []
for v in arr:
    if snt(v):
        a.append(v)
for v in a:
    if v in dic:
        dic[v] = dic[v]+1
    else:
        dic[v] = 1

for v in dic:
    print(v, dic[v])


'''

10
2 4 7 5 7 8 9 3 7 2

'''