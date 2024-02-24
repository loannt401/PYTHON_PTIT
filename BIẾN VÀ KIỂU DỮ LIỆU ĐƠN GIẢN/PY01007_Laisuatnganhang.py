t = int(input())
while t>0:
    t-=1
    s = str(input())
    lst = s.split()
    n = float(lst[0])
    x = float(lst[1])
    m = float(lst[2])

    dem = 0
    while n < m:
        n = n + n * x * 0.01
        dem += 1
    
    print(dem)


    

    