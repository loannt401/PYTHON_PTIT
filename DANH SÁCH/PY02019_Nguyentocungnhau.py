
def uscln(a, b):
    if b == 0:
        return a
    return uscln(b, a%b)

n = int(input())
a = [int(x) for x in input().split()]
a.sort()
lst = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if uscln(a[i], a[j]) == 1:
            s = str(a[i]) + " " + str(a[j])
            lst.append(s)

for v in lst:
    print(v)
    
        


'''

5
3 7 9 6 13

'''