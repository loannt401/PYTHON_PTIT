F = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

t = int(input())
while t>0:
    t-=1
    lst = input().split()
    n = int(lst[0])
    b = int(lst[1])
    s = ""
    while n > 1:
        x = int(n%b)
        s = F[x] + s
        n /= b

    print(s)
    