import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * (n + 1)]
for i in range(n):
    arr.append([0] + list(map(int, input().split())))
dp = [[[0] * 3 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 0:
            dp[i][j][0] = max(dp[i - 1][j][2], dp[i][j - 1][2]) + 1
        else:
            dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0])

        if arr[i][j] == 1 and dp[i][j][0] > dp[i][j][1]:
            dp[i][j][1] = max(dp[i - 1][j][0], dp[i][j - 1][0]) + 1
        else:
            dp[i][j][1] = max(dp[i - 1][j][1], dp[i][j - 1][1])

        if arr[i][j] == 2 and dp[i][j][1] > dp[i][j][2]:
            dp[i][j][2] = max(dp[i - 1][j][1], dp[i][j - 1][1]) + 1
        else:
            dp[i][j][2] = max(dp[i - 1][j][2], dp[i][j - 1][2])

print(max(dp[n][n]))