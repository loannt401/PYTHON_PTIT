



def usln(a, b):
    if b==0:
        return a
    return usln(b, a%b)

t = int(input())
while t>0:
    t-=1
    a = int(input())
    b = int(input())
    print(usln(a,b))
    



    

'''

1
1221
1234567891011121314151617181920212223242526272829

'''