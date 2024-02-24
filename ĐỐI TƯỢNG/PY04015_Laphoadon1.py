dem = 1
class KhachHang:
    ma = "KH"
    tongsodien = 0
    tongtien = 0

    def __init__(self, ten, cu, moi):
        global dem
        self.ten, self.cu, self.moi = ten, cu, moi
        self.ma += '{:02d}'.format(dem)
        dem += 1
        self.tongsodien = self.chisodongho()
        self.tongtien = self.Thanhtoan()

    def chisodongho(self):
        x = self.moi - self.cu
        return x
    
    def Thanhtoan(self):
        x = self.chisodongho()
        if x < 51:
            x *= 100
            x += x * 0.02
        elif x < 101:
            x = 50 * 100 + (x - 50) * 150
            x += x * 0.03
        else:
            x = 50 * 100 + 50 * 150 + (x-100) * 200
            x += x * 0.05
        return round(x)
    
    def __str__(self):
        return self.ma + " " + self.ten + " " + str(self.tongtien)

if __name__ == '__main__':
    t = int(input())
    lst = []
    while t>0:
        t-=1
        a = KhachHang(input(), int(input()), int(input()))
        lst.append(a)
    
    lst = sorted(lst, key = lambda x : -x.tongtien)
    for v in lst:
        print(v)

    


    


        

    

    
'''

3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612

'''