

t = int(input())
while t>0:
    t-=1
    lst = input().split()
    lst1 = input().split()
    lst2 = []
    for i in range(int(lst[1]), len(lst1)):
        lst2.append(lst1[i])
    for i in range(0, int(lst[1])):
        lst2.append(lst1[i])
    
    s = ""
    for v in lst2:
        s += ( v + " ")

    print(s)