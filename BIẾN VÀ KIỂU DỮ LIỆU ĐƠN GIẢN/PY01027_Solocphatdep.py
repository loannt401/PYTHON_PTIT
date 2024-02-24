



s = input()
ok = True
for i in range(len(s)-2):
    if (s[i] == '8' and s[i+1] == '8' and s[i+2] == '8') or (s[0] != '6') or (s[i] != '6' and s[i] != '8'):
        print("NO")
        ok = False
        break
if ok:
    print("YES")




'''

666666
668688
886236


'''