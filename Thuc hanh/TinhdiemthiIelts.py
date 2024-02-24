
def doiDiem(n):
    diem = 0
    if n==0: diem = 0.0
    elif n == 1 or n ==2: diem = 1.0
    elif n == 3 or n == 4: diem = 2.5
    elif n == 5 or n == 6: diem = 3.0
    elif n >= 7 and n <= 9: diem = 3.5
    elif n >= 10 and n <= 12: diem = 4.0
    elif n >= 13 and n <= 15: diem = 4.5
    elif n >= 16 and n <= 19: diem = 5.0
    elif n >= 20 and n <= 22: diem = 5.5
    elif n >= 23 and n <= 26: diem = 6.0
    elif n >= 27 and n <= 29: diem = 6.5
    elif n >= 30 and n <= 32: diem = 7.0
    elif n >= 33 and n <= 34: diem = 7.5
    elif n >= 35 and n <= 36: diem = 8.0
    elif n == 37 or n == 38: diem = 8.5
    elif n == 39 or n == 40: diem = 9.0
    return diem

t = int(input())
while t>0:
    t-=1
    lst1 = input().split()
    socau_reading = int(lst1[0])
    socau_listening = int(lst1[1])
    diem_speaking = float(lst1[2])
    diem_writing = float(lst1[3])
    diem_reading = doiDiem(socau_reading)
    diem_listening = doiDiem(socau_listening)
    diem_tb = (diem_listening + diem_reading + diem_speaking + diem_writing)/4
    lst = str(diem_tb).split(".")
    if int(lst[1][0]) >= 7 and int(lst[1][1]) >= 5:
        lst[0] = str(int(lst[0]) + 1)
        lst[1] = '0'
    elif int(lst[1][0]) >= 2 and int(lst[1][1]) >= 5:
        lst[1] = '5'
    else:
        lst[1] = '0'
    diem_tb = ".".join(lst)
    print(float(diem_tb))


