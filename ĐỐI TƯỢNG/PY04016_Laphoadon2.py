
# PY04016_Laphoadon2.py


from datetime import datetime

dem = 1
class KhangHang:
    def __init__(self, ten, phong, bd, kt, dvu):
        self.ten, self.phong, self.bd, self.kt, self.dvu = ten, phong, bd, kt, dvu

        global dem
        self.ma = "KH" + "{:02d}".format(dem)
        dem += 1

        self.tongngay = self.Tongsongay()
        self.thanhtien = self.Tongtien()


    def Tongsongay(self):
        s1 = self.bd
        s2 = self.kt
        ngay = str(datetime.strptime(s2, "%d/%m/%Y") - datetime.strptime(s1, "%d/%m/%Y"))
        ngay = ngay.split()[0]
        tong = 0
        if ngay == "0:00:00":
            tong = 1
        else:
            tong = int(ngay) + 1
        return tong

    def Tangdachon(self):
        return int(self.phong[0])

    def Tongtien(self):
        x = self.Tangdachon()
        tien = 0
        if x == 1:
            tien = 25
        elif x == 2:
            tien = 34
        elif x == 3:
            tien = 50
        else:
            tien = 80
        return self.tongngay * tien + self.dvu
    
    def __str__(self):
        return self.ma + " " + self.ten + " " + self.phong + " " + str(self.tongngay) + " " + str(self.thanhtien)

if __name__ == '__main__':
    t = int(input())
    lst = []
    while t>0:
        t-=1
        a = KhangHang(input(), input(), input().strip(), input().strip(), int(input()))
        lst.append(a)
    lst = sorted(lst, reverse=True, key= lambda x: x.thanhtien)
    for v in lst:
        print(v)





'''

3
Huynh Van Thanh   
103 
05/06/2010   
05/06/2010   
15
Le Duc Cong  
106 
08/03/2010   
01/05/2010   
220
Tran Thi Bich Tuyen   
207 
10/04/2010   
21/04/2010   
96

'''