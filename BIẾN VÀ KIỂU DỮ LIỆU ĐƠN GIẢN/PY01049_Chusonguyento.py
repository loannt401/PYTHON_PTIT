


import math


def snt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))):
        if n%i==0: return False
    return True


def soluong(s):
    dem = 0
    for v in s:
        if v == '2' or v == '3' or v == '5' or v == '7':
            dem += 1 
    if dem > (len(s)/2): return True
    return False

t = int(input())

while t>0:
    t-=1
    s = input()
    if snt(len(s)) and soluong(s):
        print("YES")
    else:
        print("NO") 
