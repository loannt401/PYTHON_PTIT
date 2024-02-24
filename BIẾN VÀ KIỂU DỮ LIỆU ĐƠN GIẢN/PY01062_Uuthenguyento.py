
import math

def snt(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def check(s):
    d1 = 0
    d2 =0
    for v in s:
        if snt(int(v)):
            d1 += 1
        else:
            d2 += 1
    if d1 <= d2:
        return False
    return snt(len(s))


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
1234567
22334455667
23400300489898989

'''