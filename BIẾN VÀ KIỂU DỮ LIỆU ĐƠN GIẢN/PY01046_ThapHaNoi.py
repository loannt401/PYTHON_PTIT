
def thapHaNoi(n,a, b, c):
    if n == 1:
        print(a + " -> " + c)
        return
    thapHaNoi(n-1,a,c,b)
    thapHaNoi(1,a,b,c)
    thapHaNoi(n-1,b,a,c)


n = int(input())
a = 'A'
b = 'B'
c = 'C'
thapHaNoi(n,a,b,c)