F = [0]*15

lst = [int(x) for x in input().split()]
k = lst[1]
a = {int(x) for x in input().split()}
n = len(a)
b = sorted(a)

def xuat():
    for i in range(1,k+1):
        print(b[F[i]-1], end=" ")
    print()

def ql(i):
    for j in range(F[i-1]+1,n-k+i+1):
        F[i] = j
        if i == k:
            xuat()
        else:
            ql(i+1)

ql(1)

    

'''

8 3
2 4 4 3 5 1 3 4

'''