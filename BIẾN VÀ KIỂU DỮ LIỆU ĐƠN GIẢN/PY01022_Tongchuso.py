s = input()

dem = 0

while True:
    if len(s) == 1: break
    tong = 0
    for v in s:
        tong += ord(v) - ord('0')
    s = str(tong)
    dem += 1

print(dem)

