
def uscln(a, b):
    if b == 0: return a
    return uscln(b,a%b)


t = int(input())
while t>0:
    t-=1
    n = int(input())
    s = str(n)
    lst = list(s)
    lst.reverse()
    s = "".join(lst)
    dao = int(s)

    if uscln(n, dao) == 1:
        print("YES")
    else:
        print("NO")
