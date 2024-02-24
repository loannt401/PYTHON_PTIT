

def cunghoangdao(ngay, thang):
    if (ngay >= 21 and ngay <= 31 and thang == 3) or (ngay >= 1 and ngay <= 19 and thang == 4): 
        return "Bach Duong"
    elif (thang == 4) or (ngay >= 1 and ngay <= 20 and thang == 5): 
        return "Kim Nguu"
    elif (thang == 5) or (ngay >= 1 and ngay <= 20 and thang == 6): 
        return "Song Tu"
    elif (thang == 6) or (ngay >= 1 and ngay <= 22 and thang == 7): 
        return "Cu Giai"
    elif (thang == 7) or (ngay >= 1 and ngay <= 22 and thang == 8): 
        return "Su Tu"
    elif (thang == 8) or (ngay >= 1 and ngay <= 22 and thang == 9): 
        return "Xu Nu"
    elif (thang == 9) or (ngay >= 1 and ngay <= 22 and thang == 10): 
        return "Thien Binh"
    elif (thang == 10) or (ngay >= 1 and ngay <= 22 and thang == 11): 
        return "Thien Yet"
    elif (thang == 11) or (ngay >= 1 and ngay <= 21 and thang == 12): 
        return "Nhan Ma"
    elif (thang == 12) or (ngay >= 1 and ngay <= 19 and thang == 1):
        return "Ma Ket"
    elif (thang == 1) or (ngay >= 1 and ngay <= 18 and thang == 2): 
        return "Bao Binh"
    else:
        return "Song Ngu"

t = int(input())

while t>0:
    t-=1
    lst = input().split()
    ngay = int(lst[0])
    thang = int(lst[1])
    print(cunghoangdao(ngay, thang))
