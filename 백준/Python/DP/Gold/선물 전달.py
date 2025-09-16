import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
tmp = [0, 0, 1, 2]
if n <= 3:
    print(tmp[n])
else:
    dp[1], dp[2], dp[3] = 0, 1, 2
    mod = 1000000000
    for i in range(4, n + 1):
        dp[i] = ((dp[i - 1] + dp[i - 2]) * (i - 1)) % mod

    print(dp[n])