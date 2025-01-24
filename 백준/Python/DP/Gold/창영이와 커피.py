import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coffee = [0] + list(map(int, input().split()))
inf = 1e7

dp = [[inf] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 0

# i - 1 이전 체크했던 커피에서 확인한다.
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j < coffee[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coffee[i]] + 1)

if dp[n][k] == inf:
    print(-1)
else:
    print(dp[n][k])