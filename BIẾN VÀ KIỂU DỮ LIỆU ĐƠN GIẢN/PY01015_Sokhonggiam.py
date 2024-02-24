t = int(input())

while t>0:
    t-=1
    s = input()
    ok = True
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            ok = False
            break

    if ok:
        print("YES")
    else :
        print("NO") 