
n = int(input())
a = [int(x) for x in input().split()]
dem = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            dem+=1
    
print(dem)


'''

5
2 4 1 3 5

'''