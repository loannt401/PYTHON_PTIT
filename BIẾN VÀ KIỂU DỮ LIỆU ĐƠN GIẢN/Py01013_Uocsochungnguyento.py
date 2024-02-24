
import math


def uscln(a,b):
    if b==0:
        return a
    return uscln(b,a%b)

def snt(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def tongchuso(n):
    s = str(n)
    tong = 0
    for v in s:
        tong += int(v)
    return tong

t = int(input())
while t>0:
    t-=1
    s = str(input())
    lst = s.split()
    if snt(tongchuso(uscln(int(lst[0]), int(lst[1])))):
        print("YES")
    else:
        print("NO")
