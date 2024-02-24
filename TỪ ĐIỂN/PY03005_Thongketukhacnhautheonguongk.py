# PY03005_Thongketukhacnhautheonguongk.py

import re

t, k = [int(x) for x in input().split()]

s = ""
while t>0:
    t-=1
    s += input() + " "

s = s.lower()
kt = '[\w]+'
lst = re.findall(pattern=kt, string=s)
dic = {}

for v in lst:
    if v not in dic:
        dic[v] = 1
    else:
        dic[v] += 1
    
a = sorted(dic, key= lambda x: (-dic[x], x))
for v in a:
    if dic[v] >= k:
        print(v, dic[v])
    else:
        break






'''

3 2
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.

'''