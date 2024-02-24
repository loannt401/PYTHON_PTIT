
n = int(input())
a = [float(x) for x in input().split()]
l = max(a)
h = min(a)
for i in range(0,n):
    if a[i] == l or a[i] == h:
        a[i] = -1
tong = 0
dem = 0
for v in a:
    if v != -1:
        tong += v
        dem += 1
print(round(tong/dem,2))

        


'''

6
6.75 8 9.2 7.25 7.75 6.75

'''