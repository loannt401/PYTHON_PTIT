t = int(input())
while t>0:
    t-=1
    s = input()
    n = input()
    solan = s.count(n, 0, len(s))
    print(solan)