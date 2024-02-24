

def sothuannghich(tong):
    x = str(tong)
    y = x[::-1]
    z = len(y)
    if (x==y and z>1): return True
    return False



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

    if sothuannghich(tong): 
        print("YES")
    else:
        print("NO")

