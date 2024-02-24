import math

def snt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

t = int(input())
while t>0:
    t-=1
    n = int(input())
    st = set()
    s = ""
    for i in range(13, n):
        d = str(i)
        i2 = int(d[::-1])
        if snt(i) and snt(i2) and i2 < n and i != i2:
            st.add(i)
            st.add(i2)
    
    lst = []
    while len(st) !=0:
        lst.append(st.pop())

    lst.sort()
    while len(lst) != 0:
        x = str(lst[0])
        s += x + " " + x[::-1] + " "
        lst.pop(0)
        lst.remove(int(x[::-1]))
    
    print(s)
    

'''

2
40
100

'''


