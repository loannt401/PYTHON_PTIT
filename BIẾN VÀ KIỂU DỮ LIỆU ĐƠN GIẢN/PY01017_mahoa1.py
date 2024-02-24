
t = int(input())
while t>0:
    t-=1
    s = input()
    dem = 0
    kq = ""
    c = s[0]
    for v in s:
        if v == c:
            dem += 1
        else:
            kq += (str(dem) + c)
            dem = 1
            c = v
    kq += (str(dem) + c)
    print(kq)


'''

3
AACDDPQ
11111147g
1111111111

'''