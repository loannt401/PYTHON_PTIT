
def tongcs(n):
    s = str(n)
    tong = 0
    for v in s:
        tong += int(v)
    return tong

t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(n):
        for j in range(i+1, n):
            if tongcs(a[i]) > tongcs(a[j]) or (tongcs(a[i]) == tongcs(a[j]) and a[i] > a[j]):
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
    s = ""
    for v in a:
        s += str(v) + " "
    print(s)




'''

1
8
143 43 22 99 7 9 1111 10000000

'''