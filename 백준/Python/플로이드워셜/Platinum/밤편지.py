import sys
input = sys.stdin.readline

n, q = map(int, input().split())
dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j, num in enumerate(list(map(int, input().split())), 1):
        if i != j and num == 0:
            dp[0][i][j] = 1e9
            continue

        dp[0][i][j] = num

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[k][i][j] = min(dp[k - 1][i][j], dp[k - 1][i][k] + dp[k - 1][k][j])

for _ in range(q):
    c, s, e = map(int, input().split())
    print(dp[c - 1][s][e] if dp[c - 1][s][e] != 1e9 else -1)

