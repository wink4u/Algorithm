import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
unknown = [0] + list(map(int, input().split()))

res = sum(unknown)
DP = [[0 for _ in range(sum(unknown) + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    byte = memory[i]
    cost = unknown[i]

    for j in range(sum(unknown) + 1):
        if j < cost:
            DP[i][j] = DP[i - 1][j]
        else:
            DP[i][j] = max(byte + DP[i - 1][j - cost], DP[i - 1][j])

        if DP[i][j] >= m:
            res = min(res, j)

print(res)