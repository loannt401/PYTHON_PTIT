

t = int(input())

def tichchuso(s):
    sum = 1
    for v in s:
        if v != '0':
            sum *= (ord(v) - ord('0'))
    return sum

while t>0:
    t-=1
    s = input()
    print(tichchuso(s))
    
'''

2
12341
123456789123456789

'''