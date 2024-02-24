
def luythua(n):
    if n == 0:
        return 1
    return n * luythua(n-1)

def tohopchapkcuan(n):
    k = 2
    ts = luythua(n)
    ms = luythua(k) * luythua(n-k)
    return ts//ms

n = int(input())
a = []
for i in range(n):
    s = input()
    a.append(s)

tong = 0
for i in range(n):
    dem = 0
    for j in range(n):
        if a[i][j] == 'C':
            dem += 1
    if dem > 1:
        tong += tohopchapkcuan(dem)

for j in range(n):
    dem = 0
    for i in range(n):
        if a[i][j] == 'C':
            dem += 1
    if dem > 1:
        tong += tohopchapkcuan(dem)

print(tong)

'''

4
CC..
C..C
.CC.
.CC.

'''