
# PY04018_Xacdinhtrungtuyen.py
dem = 1
class GiaoVien:
    def __init__(self, ten, maxt, tin, cm):
        self.ten = ten
        self.ut = self.DiemUuTien(maxt=maxt)
        self.tongdiem = self.TinhTongDiem(tin, cm)
        self.loai = self.XepLoai()
        self.ma = self.TaoMa()
        self.mon = self.Chuyenmon(maxt)
        

    
    def DiemUuTien(self, maxt):
        x = int(maxt[1])
        if x == 1:
            return 2.0
        elif x == 2:
            return 1.5
        elif x == 3:
            return 1.0
        return 0.0

    def TinhTongDiem(self, tin, cm):
        tong = tin *2 + cm + self.ut
        return round(tong, 1)

    def XepLoai(self):
        if self.tongdiem >= 18:
            return "TRUNG TUYEN"
        return "LOAI"
    
    def TaoMa(self):
        global dem
        x = "GV" + "{:02d}".format(dem)
        dem += 1
        return x

    def Chuyenmon(self, maxt):
        c = maxt[0]
        if c == 'A':
            return "TOAN"
        elif c == 'B':
            return "LY"
        return "HOA"

    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.mon} {self.tongdiem} {self.loai}"

    
if __name__ == '__main__':
    t = int(input())
    lst = []
    while t>0:
        t-=1
        lst.append(GiaoVien(input(), input(), float(input()), float(input())))
    lst = sorted(lst, reverse=True, key= lambda x: x.tongdiem)
    for v in lst:
        print(v)

        









'''

3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0

'''