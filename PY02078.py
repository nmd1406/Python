def solve(a, b, n):
    dp = [0] * (n + 1)
    res = 0

    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if (a[j] < a[i]) and (b[j] > b[i]):
                dp[i] = max(dp[i], dp[j] + 1) 
        res = max(res, dp[i])

    return res

test = int(input())
for i in range(test):
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(float, input().split())
    print(solve(a, b, n))
