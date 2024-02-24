# PY03008_Dothihinhsao.py

t = int(input())
dic = {}
for i in range(t-1):
    d1, d2 = [int(x) for x in input().split()]
    if d1 not in dic: dic[d1] = 1
    else: dic[d1] += 1
    if d2 not in dic: dic[d2] = 1
    else: dic[d2] += 1
ok = False
for v in dic:
    if dic[v] == t-1:
        print("Yes")
        ok = True
        break
if ok ==  False:
    print("No")










'''

5
1 2
1 3
1 4
1 5

'''