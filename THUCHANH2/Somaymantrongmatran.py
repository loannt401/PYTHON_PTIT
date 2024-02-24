

lst = input().split()
h = int(lst[0])
c = int(lst[1])
matran = []
l = 0
m = 10e3
for i in range(0,h):
    lst2 = input().split()
    lst3 = []
    for x in lst2:
        lst3.append(int(x))
    l1 = max(lst3)
    l = max(l,l1)
    m1 = min(lst3)
    m = min(m, m1)
    matran.append(lst3)
somayman = l-m

lst4 = []
for i in range(0,h):
    for j in range(0,c):
        if matran[i][j] == somayman:
            s = "Vi tri [" + str(i) + "][" + str(j) + "]"
            lst4.append(s)  

if(len(lst4)>0):
    print(somayman)
    for v in lst4:
        print(v)
else:
    print("NOT FOUND")




    