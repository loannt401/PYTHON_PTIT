# PY03014_Bieuthuc.py

def BieuThucDung(s):
    lst = []
    dem = 1
    for v in s:
        if v == '(':
            lst.append(dem)
            print(dem, end=" ")
            dem += 1
        elif v == ')':
            print(lst.pop(), end = " ")
    print()
            

t = int(input())
while t>0:
    t-=1
    BieuThucDung(input())



'''

2
(a + (b *c) ) + (d/e)
( ( () ) ( () ) )

'''