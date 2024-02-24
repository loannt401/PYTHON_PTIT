n = int(input())
s = input().split()
lst = []
for i in s :
    lst.append(int(i))

lst1 = []

for i in lst : 
    if len(lst1) == 0 :
        lst1.append(i)
    else :
        tong = lst1[-1] + i
        if tong % 2 == 0:
            lst1.pop(-1)
        else :
            lst1.append(i)

print(len(lst1))