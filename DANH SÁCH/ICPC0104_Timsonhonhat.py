

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

    min_val = int(lst[0])

    for v in lst:
        if min_val > int(v):
            min_val = int(v)
    print(min_val)    