
# PY04012_Tinhdiemchuyencan.py

class Chuyencan:
    
    def __init__(self, ma):
        self.ma = ma
        self.cc = 10

    def Tinhdiem(self, s):
        diem = 10
        for v in s:
            if v == 'm':
                diem -= 1
            elif v == 'v':
                diem -= 2
        return diem

    def setCc(self, s):
        self.cc = self.Tinhdiem(s)
        if self.cc <= 0:
            self.cc = 0

    def getCc(self):
        return self.cc
    
    def __str__(self):
        return self.ma + " " + str(self.cc)

class Sinhvien(Chuyencan):
    def __init__(self, ma, ten, lop):
        super().__init__(ma)
        self.ten = ten
        self.lop = lop
    
    def Kiemtra(self):
        if self.getCc == 0:
            return "KDDK"
        return ""

    def __str__(self):
        s = self.ma + " " + self.ten + " " + self.lop + " " + str(self.getCc())
        if self.getCc() == 0:
            s += " KDDK"
        return s


if __name__ == '__main__':
    t = int(input())
    lst = []
    for i in range(t):
        a = Sinhvien(input(), input(), input())
        lst.append(a)
    for i in range(t):
        s = [x for x in input().split()]
        for v in lst:
            if v.ma == s[0]:
                v.setCc(s[1])
                break
    for v in lst:
        print(v)
        


    
        


        


    

    
    
'''

3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm


'''