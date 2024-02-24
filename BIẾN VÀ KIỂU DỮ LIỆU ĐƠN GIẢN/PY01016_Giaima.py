t = int(input())
while t>0:
    t-=1
    s = input()
    s1 = ""
    for i in range(1, len(s),2):
        s1 += s[i-1]*(int(s[i]))
    print(s1)
