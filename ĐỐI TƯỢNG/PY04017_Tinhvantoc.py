
# PY04017_Tinhvantoc.py

class ThiSinh:
    def __init__(self, ten, dvi, tg):
        self.ten, self.dvi, self.tg = ten, dvi, tg

        self.thoigian = self.TongThoiGian()
        self.ma = self.MaSoThanhVien()
        self.vt = self.TongVanToc()

    def TongThoiGian(self):
        s = self.tg.split(":")
        return int(s[0]) - 6 + int(s[1])/60

    def MaSoThanhVien(self):
        a = [i[0] for i in self.ten.split()]
        b = [i[0] for i in self.dvi.split()]
        return ''.join(b) + ''.join(a)
    
    def TongVanToc(self):
        sum = 120/(self.TongThoiGian())
        return sum
        
    def __str__(self) :
        return f"{self.ma} {self.ten} {self.dvi} {round(self.vt)} Km/h"

    
if __name__ == '__main__':
    t = int(input())
    lst = []
    while t>0:
        t-=1
        a = ThiSinh(input(), input(), input())
        lst.append(a)
    lst = sorted(lst, key= lambda x: -x.vt)
    for v in lst:
        print(v)






'''

3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45

'''