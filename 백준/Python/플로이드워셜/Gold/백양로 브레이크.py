import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[1e8] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 0

for _ in range(m):
    u, v, b = map(int, input().split())
    dp[u][v] = 0
    dp[v][u] = 1 - b

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

s = int(input())

for _ in range(s):
    a, b = map(int, input().split())
    print(dp[a][b])