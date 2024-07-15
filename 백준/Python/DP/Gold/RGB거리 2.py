import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
color = [0, 1, 2]
INF = 1e12
ans = INF
for i in range(3):
    DP = [[INF, INF, INF] for _ in range(N)]
    DP[0][i] = board[0][i]

    for j in range(1, N):
        DP[j][0] = board[j][0] + min(DP[j - 1][1], DP[j - 1][2])
        DP[j][1] = board[j][1] + min(DP[j - 1][0], DP[j - 1][2])
        DP[j][2] = board[j][2] + min(DP[j - 1][1], DP[j - 1][0])

    for j in range(3):
        if i != j:
            ans = min(ans, DP[-1][j])

print(ans)
