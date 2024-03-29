
mon = ['TOAN', 'LY', 'HOA']
cong = [2, 1.5, 1, 0]

class GV :
    def __init__(self, id, ten, ma, d1, d2) :
        self.id = 'GV{0:0>2}'.format(id)
        self.ten = ten
        self.mon = mon[ord(ma[0]) - ord('A')]
        self.d = 2 * d1 + d2 + cong[int(ma[1]) - 1]
    def __str__(self) :
        s = self.id + ' ' + self.ten + ' ' + self.mon + ' ' + str(self.d)
        if self.d >= 18 : s += ' TRUNG TUYEN'
        else : s += ' LOAI'
        return s

n = int(input())
ds = []
for i in range(n) :
    ds.append(GV(i + 1, input(), input(), float(input()), float(input())))
ds = sorted(ds, key = lambda x : -x.d)
print(*ds, sep = '\n')