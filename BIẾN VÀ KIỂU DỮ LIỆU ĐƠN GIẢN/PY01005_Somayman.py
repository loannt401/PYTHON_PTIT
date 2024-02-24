s = input()
dem = 0
for v in s:
    if v == '4' or v == '7':
        dem+=1

if dem == 4 or dem==7:
    print("YES")
else :
    print("NO")