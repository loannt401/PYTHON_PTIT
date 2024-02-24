t = int(input())
while t>0:
    t-=1
    s = input()
    x1 = int(s[0:2])
    x2 = int(s[-2:])
    if x1==x2:
        print("YES")
    else:
        print("NO")