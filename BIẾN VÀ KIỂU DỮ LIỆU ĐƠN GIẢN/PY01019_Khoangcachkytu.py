

t = int(input())

while t>0:
    t-=1
    s = input()
    lst = list(s)
    lst.reverse()
    sd = "".join(lst)
    ok = True
    for i in range(len(s)-1):
        x1 = abs(ord(s[i]) - ord(s[i+1]))
        x2 = abs(ord(sd[i]) - ord(sd[i+1]))
        if x1 != x2:
            ok = False
            break

    if ok:
        print("YES")
    else:
        print("NO")

    