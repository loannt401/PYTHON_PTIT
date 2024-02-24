
def check(s):
    for v in s:
        if v != s[0] and v != s[1]: 
            return False
    for i in range(len(s)):
        if i%2==0:
            if s[i] != s[0] : return False
        else:
            if s[i] != s[1] : return False
    return True 

t = int(input())
while t>0:
    t-=1
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
