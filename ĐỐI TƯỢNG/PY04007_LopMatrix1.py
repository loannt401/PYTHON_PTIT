class Matrix:

    def __init__(self, a, n, m):
        self.a = a
        self.n = n
        self.m = m

    def matranchuyenvi(self):
        
        b = []
        for i in range(self.m):
            x = []
            for j in range(self.n):
                x.append(self.a[j][i])
            b.append(x)
        kq = Matrix(b, m, n)
        return kq

    def nhanmatran(self, p):
        kq = []
        for i in range(self.n):
            c = []  
            for j in range(self.n):
                x = 0
                for k in range(self.m):
                    x += self.a[i][k] * p.a[k][j]
                c.append(x)
            kq.append(c)
        ma = Matrix(kq, n, n)
        return ma

    def __str__(self):
        s = ''
        for i in range(self.n):
            for j in range(self.m):
                s += str(self.a[i][j]) + " "
            s += '\n'
        return s 




    
if __name__ == '__main__':
    t = int(input())
    while t>0:
        t-=1
        a = []
        lst = [int(x) for x in input().split()]
        n, m = lst[0], lst[1]
        for i in range(n):
            x = [int(x) for x in input().split()]
            a.append(x)
        
        matran = Matrix(a, n, m)
        cvi = matran.matranchuyenvi()
        tich = matran.nhanmatran(cvi)
        print(tich)





    



'''

1
2  2
1  2
3  4

'''
