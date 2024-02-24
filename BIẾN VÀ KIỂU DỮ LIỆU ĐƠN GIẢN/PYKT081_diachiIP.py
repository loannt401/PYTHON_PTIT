
t = int(input())
while t>0:
    t-=1
    s = input()
    lst = s.split(".")
    ok = True
    if len(lst) != 4 : ok = False
    else:
        for v in lst:
            if v.isnumeric():
                if int(v) > 255 or int(v) < 0 :
                    ok = False
                    break
            else: ok = False

    if ok:
        print("YES")
    else:
        print("NO")