import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
DP = [[0] * n for _ in range(n)]
DP[0][0] = 1

for i in range(n):
    for j in range(n):
        v = board[i][j]

        if v == 0 or DP[i][j] == 0:
            continue

        if i + v < n:
            DP[i + v][j] += DP[i][j]
        if j + v < n:
            DP[i][j + v] += DP[i][j]

print(DP[n - 1][n - 1])

