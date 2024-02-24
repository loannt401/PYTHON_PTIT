
def check(a, n):
    for i in range(n-1, 1, -1):
        l = 0
        r = i-1
        while l < r:
            if a[l] + a[r] == a[i]: return True
            elif a[l] + a[r] < a[i]: l+=1
            else: r -= 1
    return False

