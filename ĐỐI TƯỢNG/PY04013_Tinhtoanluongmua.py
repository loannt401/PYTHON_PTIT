
# PY04013_Tinhtoanluongmua.py

def Tongthoigian(s1, s2):
    x1 = [int(x) for x in s1.split(":")]
    x2 = [int(x) for x in s2.split(":")]
    return (x2[0]*60 + x2[1]) - (x1[0]*60 + x1[1])

class Khuvuc:
    ltb = 0
    def __init__(self, ma, ten, tg, sl):
        self.ma = "T0" + str(ma)
        self.ten, self.tg, self.sl = ten, tg, sl
        self.ltb = self.Luongmuatb()
    
    def Luongmuatb(self):
        tb = self.sl * 60 / self.tg
        return tb

    def __str__(self):
        s = self.ma + " " + self.ten + " "
        s += '{:.02f}'.format(self.ltb)
        return s
        

if __name__ == '__main__':
    t = int(input())
    dic = {}
    while t>0:
        t-=1
        ten = input()
        bd = input()
        kt = input()
        sl = int(input())
        tong = Tongthoigian(bd, kt)
        a = [tong, sl]
        if ten not in dic:
            dic[ten] = a
        else:
            b = map(lambda x1, x2: x1 + x2, a, dic[ten])
            dic[ten] = list(b)
    
    idx = 1
    for v in dic:
        ma = idx
        idx += 1
        ten = v
        tg = dic[v][0]
        sl = dic[v][1]
        a = Khuvuc(ma, ten, tg, sl)
        print(a)
    
    

        

    

    
'''

10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35

'''