t = int(input())
while t>0:
    t-=1
    s = input()
    ok = True
    for v in s:
        if v != '4' and v != '7':
            print("NO")
            ok = False
            break

    if ok:
        print("YES")