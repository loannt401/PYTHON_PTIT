
def check(s):
    if len(s)%2==0: return False
    if s[0] == s[1]: return False
    for i in range(2,len(s),2):
        if s[0] != s[i]: return False
    return True

t = int(input())

while t>0:
    t-=1
    s = input()
    if check(s): print("YES")
    else: print("NO")


    
'''

2
2324272921262
13141516

'''