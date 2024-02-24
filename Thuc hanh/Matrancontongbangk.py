

def demSoMaTran(arr, n, m, X):
    dp = [[0 for x in range(m+1)] for y in range(n+1)]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = arr[i][j]

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] += (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1])

    cnt = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            lo = 1
            hi = min(n-1, m-j) + 1

            found = False

            while lo <= hi:
                mid = (lo + hi) // 2

                ni = i + mid - 1
                nj = j + mid - 1

                sum = (dp[ni][nj] - dp[ni][j-1] - dp[i-1][nj] + dp[i-1][j-1])

                if sum >= X:
                    if sum == X:
                        found = True

                    hi = mid - 1

                else:
                    lo = mid + 1
            
            if found == True:
                cnt += 1
            
    return cnt



t = int(input())
while t>0:
    t-=1
    res = str(input()).split()
    n = int(res[0])
    m = int(res[1])
    X = int(res[2])
    maTran = []
    for i in range(n):
        s = input()
        lst = list(s)
        for i in range(len(lst)):
            lst[i] = int(lst[i])
        maTran.append(lst)
    
    print(demSoMaTran(maTran, n, m, X))









