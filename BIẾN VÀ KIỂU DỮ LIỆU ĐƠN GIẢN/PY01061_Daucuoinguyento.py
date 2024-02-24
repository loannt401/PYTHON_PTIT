
import math

def snt(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def check(s):
    x1 = int(s[0:3])
    x2 = int(s[-3:])
    if snt(x1) and snt(x2):
        return True
    return False

t = int(input())

while t>0:
    t-=1
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")

    
'''

3
12743
7337
12345678901234

'''