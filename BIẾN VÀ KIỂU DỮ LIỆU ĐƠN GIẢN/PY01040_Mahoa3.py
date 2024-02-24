P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vitri(c):
    vt = -1
    for i in range(len(P)):
        if P[i] == c:
            vt = i
            break
    return vt

def tongcackitu(s):
    tong = 0
    for v in s:
        tong += vitri(v)
    return tong

def xoayXau(s, n):
    kq = ""
    for v in s:
        x = vitri(v) + n
        x %= 26
        kq += P[x]
    return kq


def xoayKiTu(c, n):
    x = vitri(c) + n
    x %= 26
    return P[x]


t = int(input())
while t>0:
    t-=1
    s = input()
    idx = int(len(s)/2)
    s1 = s[0:idx]
    s2 = s[idx:]

    s1 = xoayXau(s1, tongcackitu(s1))
    s2 = xoayXau(s2, tongcackitu(s2))

    kq = ""
    for i in range(idx):
        kq += xoayKiTu(s1[i], vitri(s2[i]))

    print(kq)
    





