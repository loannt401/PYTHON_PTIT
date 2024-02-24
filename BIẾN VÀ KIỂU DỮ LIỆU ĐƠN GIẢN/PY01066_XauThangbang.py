def check(s):
    dao = s[::-1]
    for i in range(1,len(s)):
        kc = abs(ord(s[i])-ord(s[i-1])) - abs(ord(dao[i])-ord(dao[i-1]))
        if kc != 0:
            return False
    return True

t = int(input())

while t>0:
    t-=1
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")

    
'''

2
acxz
bcxz

'''