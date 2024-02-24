import math

class PhanSo:
    def __init__(self, ts, ms):
        self.ts= ts
        self.ms = ms
    
    def toigian(self):
        x = math.gcd(self.ts, self.ms)
        self.ts //= x
        self.ms //= x
    
    def tongPhanSo(self, p):
        self.toigian()
        p.toigian()
        self.ts = self.ts * p.ms + p.ts * self.ms
        self.ms = self.ms * p.ms
        self.toigian()

    def __str__(self):
        return str(self.ts) +'/' + str(self.ms)


if __name__ == '__main__':
    a = input().split()
    p1 = PhanSo(int(a[0]), int(a[1]))
    p2 = PhanSo(int(a[2]), int(a[3]))
    p1.tongPhanSo(p2)
    print(p1)

    



'''

123 456 12 34

'''
