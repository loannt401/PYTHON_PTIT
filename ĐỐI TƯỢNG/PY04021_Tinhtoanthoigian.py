
# PY04021_Tinhtoanthoigian.py

class Khachhang:
    tong = 0
    def __init__(self, ma, ten, bd, kt):
        self.ma, self.ten, self.bd, self.kt = ma, ten, bd, kt
        self.tong = self.Tongthoigian()
        self.thoigian = self.Chuyenvegiophut()

    def Tongthoigian(self):
        x1 = [int(x) for x in self.bd.split(':')]
        x2 = [int(x) for x in self.kt.split(':')]
        return (x2[0] * 60 + x2[1]) - (x1[0] * 60 + x1[1])
    
    def Chuyenvegiophut(self):
        x = self.Tongthoigian()
        gio = x//60
        phut = x%60
        return str(gio) + " gio " + str(phut) + " phut "
    
    def __str__(self):
        return self.ma + " " + self.ten + " " + self.thoigian

if __name__ == '__main__':
    t = int(input())
    lst = []
    while t>0:
        t-=1
        a = Khachhang(input(), input(), input(), input())
        lst.append(a)
    lst = sorted(lst, reverse= True, key= lambda x: x.tong)
    for v in lst:
        print(v)

    
    





    

    
'''

3
01T
Nguyen Van An
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00

'''