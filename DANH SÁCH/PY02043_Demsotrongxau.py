t = int(input())
while t>0:
    t-=1
    s = input()
    n = input()
    lst = s.split(n)
    print(len(lst)-1)