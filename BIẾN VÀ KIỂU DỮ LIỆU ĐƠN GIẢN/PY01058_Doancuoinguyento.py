
import math

def snt(n):
	if n < 2 : return False
	for i in range(2, int(math.sqrt(n))+1):
		if n%i==0: return False
	return True

def check(s):
    n = int(s[-4:])
    if snt(n): return True
    return False

t = int(input())

while t>0:
    t-=1
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")


    
'''

3
12234323130097
3443354654654654461123
43543543434554659999

'''