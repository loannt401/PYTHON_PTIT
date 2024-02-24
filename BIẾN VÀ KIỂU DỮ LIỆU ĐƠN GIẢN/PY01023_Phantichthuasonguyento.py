import math


t = int(input())
while t>0:
    t-=1
    n = int(input())
    s = "1 * "

    dem = 0
    while n%2==0:
        dem+=1
        n /= 2

    if dem > 0:
        s = s + "2^" + str(dem) 
        if n > 1: s = s + " * "

    i = 3
    while n>1:
        if n%i==0:
            dem = 0
            while(n%i==0):
                dem+=1
                n /= i
            
            s = s + str(i) + "^" + str(dem)
            if n>1: s += " * "
        
        else:
            i+=2

    
    print(s)
        