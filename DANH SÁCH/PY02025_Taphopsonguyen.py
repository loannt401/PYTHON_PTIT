
def xuat(x):
    for v in x:
        print(v, end=" ")
    print()

lst = [int(x) for x in input().split()]
a = {int(x) for x in input().split()}
b = {int(x) for x in input().split()}
giao = a & b
hieu1 = a - b
hieu2 = b - a
res1 = sorted(giao)
res2 = sorted(hieu1)
res3 = sorted(hieu2)
xuat(res1), xuat(res2), xuat(res3)
   
    
    

    



'''

5 6
1 2 3 4 5
3 4 5 6 7 8

'''