import math

def snt(n):
    if n<2: return False
    for i in range (2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

t = int(input())

while t>0:
    t-=1
    n = int(input())
    dem = 0
    for i in range(n-6):
        if snt(i) and snt(i+2) and snt(i+6):
            dem +=1
        if snt(i) and snt(i+4) and snt(i+6):
            dem += 1

    print(dem)


    '''
    
2
15
25
    
    '''
