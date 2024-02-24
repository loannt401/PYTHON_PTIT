

t = int(input())
lst = []
while t>0:
    t-=1;
    s = input();
    if s not in lst:
        lst.append(s);

print(len(lst));
