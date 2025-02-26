import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        move = board[i][j]

        if board[i][j]:
            if move + i < n:
                dp[i + move][j] += dp[i][j]

            if move + j < n:
                dp[i][j + move] += dp[i][j]

print(dp[n - 1][n - 1])