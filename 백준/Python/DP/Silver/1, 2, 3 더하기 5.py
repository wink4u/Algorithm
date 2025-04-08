import sys
input = sys.stdin.readline

t = int(input())

dp = [[0] * 3 for _ in range(100001)]
dp[1][0] = 1
dp[2][1] = 1
dp[3] = [1, 1, 1]

mod = 1000000009
for i in range(4, 100001):
    for j in range(1, 4):
        if j == 1:
            dp[i][j - 1] += dp[i - j][1]
            dp[i][j - 1] += dp[i - j][2]
        elif j == 2:
            dp[i][j - 1] += dp[i - j][0]
            dp[i][j - 1] += dp[i - j][2]
        else:
            dp[i][j - 1] += dp[i - j][0]
            dp[i][j - 1] += dp[i - j][1]

        dp[i][j - 1] %= 1000000009

for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % 1000000009)
