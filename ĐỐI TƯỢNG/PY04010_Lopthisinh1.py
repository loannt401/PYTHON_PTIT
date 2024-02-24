
class ThiSinh:
    tong = 0
    def __init__(self, ten, ns, d1, d2, d3):
        self.ten, self.ns, self.d1, self.d2, self.d3 = ten, ns, d1, d2, d3

    def __str__(self):
        self.tong = self.d1 + self.d2 + self.d3
        self.tong = round(self.tong,1)
        return self.ten + " " + self.ns + " " + str(self.tong)

if __name__ == '__main__':
    a = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
    print(a)

        


    
    

    
'''

Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5

'''