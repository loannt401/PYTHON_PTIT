



t = int(input())
while t>0:
    t-=1
    s = input()
    a = []
    tong = 0
    for v in s:
        if v.isdigit():
            tong += int(v)
        else:
            a.append(v)
    a.sort()
    for v in a:
        print(v, end="")
    print(tong)





'''

2
AC2BEW3
ACCBA10D2EW30


'''