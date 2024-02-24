
class Rectangle:
    def __init__(self, dai, rong, ms):
        self.dai = dai
        self.rong = rong
        self.ms = ms
    
    def perimeter(self):
        return 2 * (self.dai + self.rong)
    
    def area(self):
        return self.dai * self.rong
    
    def color(self):
        s = self.ms.title()
        return s



arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')
    

'''

10 2 RED

'''
