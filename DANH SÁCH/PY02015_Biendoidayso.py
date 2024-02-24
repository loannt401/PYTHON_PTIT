
def check(a):
    for i in range(1,4):
        if a[i] != a[i-1]:
            return False
    return True

while True:
    a = [int(x) for x in input().split()]
    if a == [0,0,0,0]:
        break
    dem = 0
    while check(a) == False:
        tmp = a[0]
        for i in range(3):
            a[i] = abs(a[i] - a[i+1])
        a[3] = abs(a[3] - tmp)

        dem += 1
    print(dem)
    

        
    
        


'''

1 3 5 9
4 3 2 1
0 0 0 0

'''