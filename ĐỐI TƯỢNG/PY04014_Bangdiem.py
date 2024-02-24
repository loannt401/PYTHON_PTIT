
dem = 1
class Hocsinh:
    msh = ""
    tong = 0
    loai = ""
    def __init__(self, ten, diem):
        global dem
        s = "HS"
        if dem < 10:
            s += "0" 
        s += str(dem)
        dem = dem + 1
        self.msh = s
        self.ten = ten
        self.diem = diem
        self.tong = self.diemTb()
        self.loai = self.xeploai()
    
    def diemTb(self):
        tb = (self.diem[0] + self.diem[1]) * 2
        for i in range(2, len(self.diem)):
            tb += self.diem[i]
        tb /= 12
        return round((tb*100 + 1)/100,1)

    def xeploai(self):
        x = self.diemTb()
        if x >= 9:
            return 'XUAT SAC'
        elif x >= 8:
            return 'GIOI'
        elif x >= 7:
            return 'KHA'
        elif x >= 5:
            return 'TB'
        else:
            return 'YEU'

    def __str__(self):
        return self.msh + " " + self.ten + " " + str(self.tong) + " " + self.loai


if __name__ == '__main__':
    t = int(input())
    lst = []
    while t>0:
        t -= 1
        ten = input()
        diem = [float(x) for x in input().split()]
        a = Hocsinh(ten, diem)
        lst.append(a)
    
    lst1 = sorted(lst, key= lambda x : (- x.tong, x.msh))
    for v in lst1:
        print(v)


    



        

    

    
'''

3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0

'''