


import math


def snt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))):
        if n%i==0: return False
    return True

t = int(input())

while t>0:
    t-=1
    s = input()
    n = int(s[-4:])
    if snt(n): print("YES")
    else: print("NO")
