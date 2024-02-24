


s = str(input())
lst = s.split()
a = int(lst[0])
k = int(lst[1])
n = int(lst[2])


s = ""
for i in range(k, n+1,k):
    if i <= a: continue
    else :
        s += (str(i-a) + " ")
    

if s == "":
    print(-1)
else:
    print(s)