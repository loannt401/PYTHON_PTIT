

n = 10
i = 0
a = set()
while i<10:
    s = input().split()
    i += len(s)
    for v in s:
        a.add(int(v)%42)
print(len(a))


'''

1 2 3 4 5 6  7 8  9 10

42 84 252 420 840
126 42 84 420 126

39 40 41 42 43 44 82
83 84 85

'''


