import sys
input = sys.stdin.readline

n = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    day, value = arr[i]

    if i + day - 1 <= n:
        dp[i + day - 1] = max(dp[i - 1] + value, dp[i + day - 1])

print(dp[-1])