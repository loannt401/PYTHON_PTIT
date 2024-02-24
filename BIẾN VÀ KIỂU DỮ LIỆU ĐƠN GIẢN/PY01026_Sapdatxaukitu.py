

n = int(input())
for i in range(1, n+1):
    n-=1
    s1 = [x for x in input()]
    s2 = [x for x in input()]
    s1.sort()
    s2.sort()
    print("Test " + str(i) + ":", end=" ")
    if s1 == s2:
        print("YES")
    else:
        print("NO")



    

'''

4
testing
intestg
abc
aabbbcccc
abcabcbcc
aabbbcccc
abc
xyz

'''