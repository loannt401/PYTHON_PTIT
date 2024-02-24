P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."


def vitri(s):
    vt = -1
    for i in range(len(P)):
        if P[i] == s:
            vt = i
            break
    return vt

while True:
    s = input()
    if s == '0':
        break
    lst = s.split()
    k = int(lst[0])
    xau = lst[1]
    kq = ""
    for v in xau:
        vt = (vitri(v) + k)%28
        kq += P[vt]
    lst2 = list(kq)
    lst2.reverse()
    kq = "".join(lst2)
    print(kq)


