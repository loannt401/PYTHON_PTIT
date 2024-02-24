
# PY04020_Laphoadon3.py
dem = 1
class MatHang:
    ma = str()
    ten = str()
    sl = int()
    gia = int()
    chieukhau = int()
    tongtien = int()
    def __init__(self, ma, ten, sl, gia, chietkhau):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.gia = gia
        self.chieukhau = chietkhau
        self.tongtien = self.TinhTongTien()
    
    def TinhTongTien(self):
        return self.sl * self.gia - self.chieukhau
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.sl} {self.gia} {self.chieukhau} {self.tongtien}"

    
if __name__ == '__main__':
    t = int(input())
    lst = []
    while t>0:
        t-=1
        lst.append(MatHang(input(), input(), int(input()), int(input()), int(input())))
    lst = sorted(lst, reverse=True, key= lambda x: x.tongtien)
    for v in lst:
        print(v)

        









'''

3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000

'''