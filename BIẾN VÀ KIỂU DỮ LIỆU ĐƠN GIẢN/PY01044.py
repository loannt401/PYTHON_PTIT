
s1 = {x.lower() for x in input().split()}
s2 = {x.lower() for x in input().split()}
hop = s1 | s2
giao = s1 & s2
h = sorted(hop)
g = sorted(giao)
for v in h:
    print(v, end=" ")
print()
for v in g:
    print(v, end=" ")
print()




'''

Lap trinh huong doi tuong
Ngon ngu lap trinh C++

PY01044


'''