t = int(input())
while t>0:
    t-=1
    s = input()
    x = s[-2:]
    if x == '86':
        print("YES")
    else:
        print("NO")