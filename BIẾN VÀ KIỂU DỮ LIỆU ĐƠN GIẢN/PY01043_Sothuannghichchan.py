
def check(n):
    s = str(n)
    if len(s) % 2 == 1: return False
    l = 0
    r = len(s)-1
    for v in s:
        if int(v) % 2 != 0: return False
        
    while l < r:
        if s[l] != s[r]: return False
        l+=1
        r-=1
    return True

t = int(input())
while t>0:
    t-=1
    kq = ""
    n = int(input())
    for i in range(22,n,22):
        if check(i):
            kq += (str(i) + " ")
    print(kq)