
def uscln(a, b):
    if b == 0: return a
    return uscln(b,a%b)

s = str(input())
lst = s.split()
n = int(lst[0])
k = int(lst[1])

kq = ""
xau = []

batdau = pow(10,k-1)
ketthuc = pow(10,k)

dem = 0
for i in range(batdau, ketthuc):
    if uscln(n,i) == 1:
        if dem < 10:
            kq += (str(i) + " ")
            dem+=1
        else:
            print(kq)
            kq = (str(i) + " ")
            dem = 1

print(kq)


