import math

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i==0:
            return False
    return True

F = []
i = 2
while len(F) <= 1000:
    if snt(i):
        F.append(i)
    i += 1

lst = [int(x) for x in input().split()]
n = lst[0]
x = lst[1]

res = str(x) + " "
for i in range(n):
    x = x + F[i]
    res += str(x) + " "
print(res)


'''

5 4

'''


