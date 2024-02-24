

t = int(input())
while t>0:
    t-=1
    n= int(input())
    a = input().split()
    lst = []
    for x in a:
        lst.append(int(x))
    l = max(lst)
    m = min(lst)
    lst2 = []
    for i in range(0,l+1):
        lst2.append(0)
    for i in range(0, len(lst)):
        x = lst[i]
        lst2.pop(x)
        lst2.insert(x,1)
    dem = 0
    for i in range(m,l+1):
        if lst2[i] == 0: dem+=1
    print(dem)
    
