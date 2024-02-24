
def tichcs(n):
    s = str(n)
    tich = 1
    for v in s:
        tich *= int(v)
    return tich

t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(n):
        for j in range(i+1, n):
            if tichcs(a[i]) > tichcs(a[j]) or (tichcs(a[i]) == tichcs(a[j]) and a[i] > a[j]):
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