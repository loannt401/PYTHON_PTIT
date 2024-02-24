
lst = input().split()
L = int(lst[0])
R = int(lst[1])
X = [L-1, 0, 0, 0]

def uscln(a, b):
    if b== 0: return a
    return uscln(b, a%b)

def sntCungNhau(a, b, c):
    if uscln(a,b) == 1 and uscln(b,c)==1 and uscln(a,c)==1:
        return True
    return False

def xuat():
    if sntCungNhau(X[1], X[2], X[3]):
        res = X.copy()
        res.pop(0)
        kq = tuple(res)
        print(kq)


def quaylui(i):
    for j in range(X[i-1]+1, R+1-3+i):
        X[i] = j
        if i == 3: xuat()
        else: quaylui(i+1)

quaylui(1)

 

