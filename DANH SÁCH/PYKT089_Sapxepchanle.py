
n = int(input())
a = []
while len(a) < n:
    s = input()
    for v in s.split():
        a.append(int(v))
c = []
c1 = []
l = []
l1 = []
for i in range(n):  
    if a[i] % 2 == 0:
        c.append(a[i])
        c1.append(i)
    else:
        l.append(a[i])
        l1.append(i)
c.sort()
l.sort()
l.reverse()
for i in range(len(c)):
    a[c1[i]] = c[i]
for i in range(len(l)):
    a[l1[i]] = l[i]
for v in a:
    print(v, end = " ")
print()


'''

10
1 2 3 4 5 6 7 7 9 6

'''