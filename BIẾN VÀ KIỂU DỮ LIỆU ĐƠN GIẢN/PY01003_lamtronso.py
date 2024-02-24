t = int(input())

while t>0:
    t-=1
    s = input()
    n = len(s)-1
    while n > 0:
        if int(s[n]) >= 5:
            if int(s[n]) == 9:
                tmp = len(s) - 1 - n
                x = int(s) + 10**tmp
                s = str(x)
            else:
                s = s[0:n-1] + str(int(s[n-1]) + 1) + '0'*(len(s) - n)
        else:
            s = s[0:n] + '0'*(len(s) - n)
        n = n - 1
    print(int(s))



# t = int(input())
# while t>0:
# 	t-=1
# 	n = int(input())
# 	sl = len(str(n))
# 	for i in range(1,sl):
# 		s = list(str(n))
# 		if s[sl-i] == '5':
# 			s[sl-i] = '6'
# 		s = "".join(s)
# 		n = int(s)
# 		n = round(n, -i)
# 	print(n)
'''

7
15
14
5
99
12345678
44444445
1445

'''

