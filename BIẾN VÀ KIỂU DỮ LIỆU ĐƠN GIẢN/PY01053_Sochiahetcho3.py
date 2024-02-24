
def chiahet3(n):
    if n%3==0: return True
    return False

t = int(input())

def tongchuso(s):
    sum = 0
    for v in s:
        sum += (ord(v) - ord('0'))
    if chiahet3(sum): return True
    return False

while t>0:
    t-=1
    s = input()
    if tongchuso(s): print("YES")
    else: print("NO")
    
'''

2
12341
123456789123456789

'''