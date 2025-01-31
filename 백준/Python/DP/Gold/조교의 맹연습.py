import sys
input = sys.stdin.readline

# 좌, 우, 뒤, 총량
a, b, c, k = map(int, input().split())

cost = [a, b, c]
dp = [[1e9] * 4 for _ in range(k + 1)]
d = [3, 1, 2]

dp[0][0] = 0

for i in range(k + 1):
    for j in range(4):
        if dp[i][j] == 1e9:
            continue

        for c in range(3):
            if i + cost[c] > k:
                continue
            dp[i + cost[c]][(j + d[c]) % 4] = min(dp[i + cost[c]][(j + d[c]) % 4], dp[i][j] + 1)

print(dp[k][0] if dp[k][0] != 1e9 else -1)