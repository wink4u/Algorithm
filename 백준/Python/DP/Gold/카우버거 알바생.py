import sys
input = sys.stdin.readline

# 치즈버거 m, 감자튀김 k
n, m, k = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(k + 1)]

for _ in range(n):
    x, y = map(int, input().split())

    if m < x or k < y:
        continue

    for i in range(k, y - 1, -1):
        for j in range(m, x - 1, -1):
            dp[i][j] = max(dp[i - y][j - x] + 1, dp[i][j])

print(dp[k][m])