
t = int(input())
while t>0:
    t-=1
    s = input().split()
    kq = ""
    for v in s:
        if len(kq) + len(v) + 1 <= 100:
            kq += v + " "
        else:
            break
    print(kq)






'''

2
Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021
Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen

'''