def tong(s):
    sum = 0
    for i in range(len(s)):
        if i %2==0:
            sum += int(s[i])
    return sum

def tich(s):
    sum = 1
    ok = 0
    for i in range(len(s)):
        if i % 2 != 0 and s[i] != '0':
            sum *= int(s[i])
            ok = 1
    if ok == 1: return sum
    return 0

t = int(input())

while t>0:
    t-=1
    s = input()
    print(tong(s), tich(s))


    
'''

3
12345678
20000
22334455667788

'''