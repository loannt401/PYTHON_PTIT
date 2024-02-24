

F = [0*x for x in range(94)]
F[1] = 1
i=2
while i<=93 :
    F[i] = F[i-1] + F[i-2]
    i+=1

t = int(input())
while t>0:
    t-=1
    lst = [ int(x) for x in input().split()]
    s = ""
    for i in range(lst[0], lst[1]+1):
        s += str(F[i]) + " "

    print(s) 



'''

1
1 10

'''


