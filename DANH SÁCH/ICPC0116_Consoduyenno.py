t = int(input())

while t>0:
    t-=1
    lst = list(input())
    if(lst[0] == lst[len(lst)-1]): print("YES")
    else: print("NO")