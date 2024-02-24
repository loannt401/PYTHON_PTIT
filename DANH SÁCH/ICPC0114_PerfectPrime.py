import math

def snt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

def check(s):
    for v in s:
        if snt(int(v)) == False: return False
    return True

t = int(input())
while t>0:
    t-=1
    n = int(input())
    s = str(n)
    d = int(s[::-1])
    if snt(n) and snt(d) and check(s):
        print("Yes")
    else:
        print("No")

'''

3
13
753
757

'''
