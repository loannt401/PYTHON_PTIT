
def giaithua(n):
    tong = 1
    for i in range(1,n+1):
        tong *= i
    return tong

t = int(input())
while t>0:
    t-=1
    n = int(input())
    s = str(n)
    tong = 0
    for v in s:
        tong += giaithua(int(v))
    if tong == n:
        print('Yes')
    else:
        print('No')

'''

2
145
235

'''