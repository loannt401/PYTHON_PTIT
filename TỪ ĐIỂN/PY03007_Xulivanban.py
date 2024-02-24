
# PY03007_Xulivanban.py

import re

text = ""
while True:
    try:
        s = input()
        text += s + ""
    except EOFError:
        break


pattern = '[\s\w,:]+'

result = re.findall(pattern=pattern, string=text)

for v in result:
    lst = v.split()
    a = " ".join(lst)
    a = a[0].upper() + a[1:].lower()
    print(a)






'''

ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
    vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.

'''
