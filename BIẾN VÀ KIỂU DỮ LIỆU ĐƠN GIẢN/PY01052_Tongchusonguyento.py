import math
def snt(n):
    if(n<2):
        return False
    i=2
    while i <= math.sqrt(n):
        if(n%i == 0): 
            return False
        i+=1
    return True 


t = int(input())

while t>0:
    t-=1
    lst = list(input())
    lst1 = []
    for v in lst:
        lst1.append(int(v))
    tong = 0
    for v in lst1:
        tong += v

    if snt(tong): 
        print("YES")
    else:
        print("NO")

