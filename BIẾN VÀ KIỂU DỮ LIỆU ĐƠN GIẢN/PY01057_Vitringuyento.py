
import math

'''

F = [2, 3, 5, 7]

def snt(n):
    if n in F: return True
    return False

=> không thể dùng cách này vì có thể độ dài chữ số >10

'''
def snt(n):
	if n < 2 : return False
	for i in range(2, int(math.sqrt(n))+1):
		if n%i==0: return False
	return True

def check(s):
    for i in range(len(s)):
        if snt(i) != snt(int(s[i])): 
            return False
    return True

t = int(input())

while t>0:
    t-=1
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")


    
'''

2
14239567
2314514535353

'''