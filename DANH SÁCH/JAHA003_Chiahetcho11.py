

t = int(input())

while t>0:
    t-=1
    lst = list(input())
    lst2 = []
    for v in lst:
        lst2.append(int(v))
    tong1 = 0
    tong2 = 0
    for i in range(0, len(lst2),2):
        tong1 += lst2[i]
    for i in range(1,len(lst2),2):
        tong2 += lst2[i]
    x = tong1 - tong2
    if x%11==0: print("YES")
    else: print("NO")