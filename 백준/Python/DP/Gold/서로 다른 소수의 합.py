import sys
input = sys.stdin.readline

t = int(input())
prime = []
dp = [[0] * 15 for _ in range(1121)]

for i in range(2, 1121):
    flag = 0
    for j in range(2, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            flag = 1
            break

    if not flag:
        prime.append(i)

dp[0][0] = 1
for p in prime:
    for i in range(1120, p - 1, -1):
        for j in range(14, 0, -1):
            dp[i][j] += dp[i - p][j - 1]

for _ in range(t):
    n, k = map(int, input().split())
    print(dp[n][k])