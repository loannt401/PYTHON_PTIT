
import math

def check(s):
    for i in range(len(s)):
        if i%2==0:
            if (ord(s[i])-ord('0'))%2!=0: return False
        else:
            if (ord(s[i])-ord('0'))%2==0: return False
    return True
        

def snt(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))):
        if n%i==0: return False
    return True

def tongchuso(s):
    sum = 0
    for v in s:
        sum += (ord(v) - ord('0'))
    if snt(sum): return True
    return False

    

t = int(input())

while t>0:
    t-=1
    s = input()
    if tongchuso(s) and check(s):
        print("YES")
    else:
        print("NO")


    
'''

2
2345678521
1212121212121212121212121

'''