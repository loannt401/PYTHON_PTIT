
idx = 1

def chuyendoidiem(x):
    if x <= 10.0:
            return x
    return x/10
        

class Nhanvienmoi:
    ma = "TS0"
    dtb = 0
    loai = ""
    def __init__(self, ten, lt, th):
        self.ten = ten
        self.lt = chuyendoidiem(lt)
        self.th = chuyendoidiem(th)

        global idx
        self.ma += str(idx)
        idx += 1

        self.dtb = self.DiemTrungBinh()
        self.loai = self.XepLoai()


    def DiemTrungBinh(self):
        return round((self.lt + self.th)/2, 2)

    def XepLoai(self):
        x = self.DiemTrungBinh()
        if x < 5: 
            return "TRUOT"
        elif x < 8:
            return "CAN NHAC"
        elif x <= 9.5:
            return "DAT"
        return "XUAT SAC"

    def __str__(self):
        return self.ma + " " + self.ten + " " + '{:.02f}'.format(self.dtb) + " " + self.loai

    
if __name__ == "__main__":
    t = int(input())
    lst = []
    while t>0:
        t-=1
        a = Nhanvienmoi(input(), float(input()), float(input()))
        lst.append(a)
    lst = sorted(lst, reverse= True, key = lambda x: x.dtb)

    for v in lst:
        print(v)



    


    


    


        

    

    
'''

3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56

'''