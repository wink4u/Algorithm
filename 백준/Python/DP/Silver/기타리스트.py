import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())
song = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m + 1):
        if dp[i][j]:
            if j + song[i] <= m:
                dp[i + 1][j + song[i]] = 1

            if j - song[i] >= 0:
                dp[i + 1][j - song[i]] = 1

res = -1

for i in range(m, -1, -1):
    if dp[n][i]:
        res = i
        break

print(res)