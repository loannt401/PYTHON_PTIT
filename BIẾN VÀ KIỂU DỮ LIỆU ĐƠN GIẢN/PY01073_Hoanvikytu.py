



s = input()
n = len(s)

F = [0]*(n+1)
ok = [0]*(n+1)

def xuat():
    for i in range(1, n+1):
        print(s[F[i]-1], end="")
    print()

def ql(i):
    for j in range(1,n+1):
        if ok[j] == 0:
            F[i] = j
            ok[j] = 1
            if i == n:
                xuat()
            else:
                ql(i+1)
            ok[j] = 0

ql(1)
    



    

'''

XYZ

'''