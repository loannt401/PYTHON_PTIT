

n = int(input())

for i in range(n):
    s = input()
    res = ""
    for i in s:
        if i.isnumeric() :
            res += i
        else:
            res += " "
    lst = res.split()

    max_val = int(lst[0])

    for v in lst:
        if max_val < int(v):
            max_val = int(v)
    print(max_val)    