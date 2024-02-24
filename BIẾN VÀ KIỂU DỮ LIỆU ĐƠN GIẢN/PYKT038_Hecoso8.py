F = ['000', '001', '010', '011', '100', '101', '110', '111']

s = input()
while len(s)%3 != 0:
    s = '0' + s
s = " " + s
kq = ""
for i in range(len(s)-3, 0, -3):
    x = s[i:i+3]
    for i in range(8):
        if F[i] == x:
            kq = str(i) + kq
            break

print(kq)
