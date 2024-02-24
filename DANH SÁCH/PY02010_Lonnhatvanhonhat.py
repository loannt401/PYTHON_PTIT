
while True:
    n = int(input())
    if n == 0:
        break
    else:
        st = set()
        for i in range(n):
            x = int(input())
            st.add(x)
        ma = max(st)
        mi = min(st)
        if ma == mi:
            print("BANG NHAU")
        else:
            print(mi, ma)



'''

5
1
2
3
4
5
3
001
22
33333333333333333333333333333333333
3
1
1
1
0

'''