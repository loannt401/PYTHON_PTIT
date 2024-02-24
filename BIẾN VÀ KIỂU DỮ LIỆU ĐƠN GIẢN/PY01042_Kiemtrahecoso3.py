
def check(s):
    for v in s:
        if v != '0' and v != '1' and v != '2':
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