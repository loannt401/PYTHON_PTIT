
class Sophuc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def kqC(self):
        return (self.a + self.b) * self.a

    def kqD(self):
        return (self.a + self.b)**2


def xuat(a):
    thuc = a.real
    if thuc == int(thuc): thuc = int(thuc)
    ao = a.imag
    if ao == int(ao): ao = int(ao)
    ao = str(ao)

    s = str(thuc)
    if ao[0] == '-':
        s += ' - ' + ao[1:]
    else:
        s += ' + ' + ao
    s += "i"
    return s
    

if __name__ == '__main__':
    t = int(input())
    while t>0:
        t-=1
        arr = [float(x) for x in input().split()]
        a = complex(arr[0], arr[1])
        b = complex(arr[2], arr[3])
        tong = Sophuc(a,b)
        print(xuat(tong.kqC()) + ", " + xuat(tong.kqD()))

        


    
    

    
'''

3
1 2 3 4
2 3 4 5
1 -2 5 -6

'''