

def check(a, b):
    for v in a:
        if v in b:
            b.remove(v)
    if len(b) == 0: return True
    return False

t = int(input())
k = 0
while t>0:
    t-=1
    k+=1
    s1 = input()
    s2 = input()
    if len(s1) != len(s2):
        print("Test "+ str(k) + ": NO")
    else:
        lst1 = list(s1)
        lst2 = list(s2)
        if check(lst1, lst2):
            print("Test "+ str(k) + ": YES")
        else:
            print("Test "+ str(k) + ": NO")


