
import math


def snt(n):
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

n = int(input())
a = input().split()

b = []
for v in a:
    if len(b) == 0: b.append(int(v))
    else :
        if int(v) not in b: b.append(int(v))

tong = 0
for v in b: tong += v

vt = -1
tong1 = 0

for i in range(len(b)):
    tong1 += b[i]
    tong2 = tong - tong1
    if snt(tong1) and snt(tong2):
        vt = i
        break

if vt < 0 : print("NOT FOUND")
else: print(vt) 
