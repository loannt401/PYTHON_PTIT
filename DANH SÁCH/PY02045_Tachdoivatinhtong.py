s = input()
while True:
    if len(s) == 1: break
    idx = int(len(s)/2)
    s1 = s[:idx]
    s2 = s[idx:]
    s = str(int(s1) + int(s2))
    print(s)
