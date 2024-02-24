
def doicoso(s, n):
    while len(s)%n != 0:
        s = '0' + s
    res = ''
    x = 0
    for i in range(len(s)):
        x += int(s[i]) * 2**(n - (i%n) - 1)
        if(i+1)%n==0:
            if x == 10: res += 'A'
            elif x == 11: res += 'B'
            elif x == 12: res += 'C'
            elif x == 13: res += 'D'
            elif x == 14: res += 'E'
            elif x == 15: res += 'F'
            else: res += str(x)
            x = 0
    return res



t = int(input())
while t>0:
    t-=1
    k = int(input())
    s = input()
    i = 0
    if(k==2): i=1
    elif k == 4: i = 2
    elif k == 8: i = 3
    else: i = 4

    print(doicoso(s,i))

'''

2
8
10010100010010101
2
10010100010010101

'''