



s = input()
while len(s) % 3 != 0:
    s = '0' + s

x = 0
for i in range(len(s)):
    x += (2**(3 - (i)%3 - 1)) * int(s[i])
    if (i+1) % 3 == 0:
        print(x, end= "")
        x = 0




'''

11001100


'''