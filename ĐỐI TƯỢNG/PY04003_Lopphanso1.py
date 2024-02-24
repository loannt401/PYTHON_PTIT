
def uscln(a, b):
        if b == 0:
            return a
        return uscln(b, a%b)

class PhanSo:
    def __init__(self, ts, ms):
        self.ts = ts
        self.ms = ms
    
    def toigian(self):
        a = int(self.ts)
        b = int(self.ms)
        x = uscln(a, b)
        self.ts = str(a//x)
        self.ms = str(b//x)
    
    def __str__(self):
        self.toigian()
        return self.ts + "/" + self.ms

if __name__ == '__main__':
    arr = input().split()
    p = PhanSo(arr[0], arr[1])
    print(p)


'''

123 456

'''
