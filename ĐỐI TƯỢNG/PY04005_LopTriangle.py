from decimal import Decimal
import math

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def distance(self, p):
        x = math.sqrt((self.a - p.a)**2 + (self.b - p.b)**2)
        x = Decimal(str(x) +"000")
        return round(x, 4)

    
def chuvi(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        cv = a + b + c
        cv = Decimal(str(cv) + '000')
        print(round(cv, 3))
    else:
        print("INVALID")




if __name__ == '__main__':
    t = int(input())
    arr = []
    for i in range(t):
        arr += input().split()
    
    i = 0
    while t>0:
        t-=1
        p1 = Point(Decimal(arr[i]), Decimal(arr[i+1]))
        p2 = Point(Decimal(arr[i+2]), Decimal(arr[i+3]))
        p3 = Point(Decimal(arr[i+4]), Decimal(arr[i+5]))
        a = p1.distance(p2)
        b = p1.distance(p3)
        c = p2.distance(p3)
        chuvi(a, b, c)
        i+=6




    



'''

3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0

'''
