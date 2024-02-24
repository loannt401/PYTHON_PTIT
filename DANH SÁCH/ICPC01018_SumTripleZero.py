t = int(input())

while(t>0):
    t-=1
    n = int(input())
    s = input().split()
    lst = []
    for v in s:
        lst.append(int(v))

    lst.sort()
    dem = 0
    for i in range(0,n-2):
        tong = 0 - lst[i]
        l = i+1
        r = n-1
        while l<r:
            if lst[l] + lst[r] == tong:
                dem += 1
                l+=1
            elif lst[l] + lst[r] < tong:
                l+=1
            else: 
                r-=1
    
    print(dem)


'''

2
5
0 -1 2 -3 1 
5
1 -2  1  0  5

 đề bài sai: có tồn tại số nguyên giống nhau
 nên: lst[l] + lst[r] == tong chỉ có l+=1 không có r-=1 

'''