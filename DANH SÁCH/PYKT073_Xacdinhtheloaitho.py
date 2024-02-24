
t = int(input())
a = []
while t > 0:
    t-=1
    s = input()    
    a.append(len(s.split()))
    s = ""

for i in range(len(a)):
    if a[i] == 6 or a[i] == 8:
        a[i] = 1
    else: 
        a[i] = 2

lst = []
val = a[0]
dem = 0
for v in a:
    if v == val :
        dem += 1
    else:
        x = [val, dem]
        lst.append(x)
        val = v
        dem = 1
x = [val, dem]
lst.append(x)

lst1 = []
for v in lst:
    if v[0] == 1:
        lst1.append(1)
    else:
        for i in range(v[1]//4):
            lst1.append(2)

print(len(lst1))
for v in lst1:
    print(v)   





'''

8
Minh ve minh co nho ta
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong
Nhin cay nho nui nhin song nho nguon
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay

'''