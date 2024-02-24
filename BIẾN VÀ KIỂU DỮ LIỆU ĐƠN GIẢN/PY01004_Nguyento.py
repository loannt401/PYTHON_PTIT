
import math






def snt(n):
    if n<2: 
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if (n % i) == 0: 
            return False
    return True


t = int(input())
while(t>0):
    t-=1
    n = int(input())
    dem = 0
    for i in range(1,n):
        if uscln(n,i) == 1:
            dem+=1
    
    if snt(dem):
        print("YES")
    else :
        print("NO")




    
