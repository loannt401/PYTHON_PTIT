s = input()
kq = ""
for i in range(len(s)-3,0,-3):
    kq = s[:i] + "," + s[i:]
    s = kq    

print(s)

