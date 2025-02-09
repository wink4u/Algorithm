import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
visit = [[-1] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = [list(map(int, input().split())) for _ in range(n)]

res = 1
def dfs(x, y):
    global res

    if visit[x][y] != -1:
        return visit[x][y]

    visit[x][y] = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and board[x][y] < board[nx][ny]:
            count = dfs(nx, ny) + 1
            visit[x][y] = max(visit[x][y], count)
            res = max(res, visit[x][y])

    return visit[x][y]

for i in range(n):
    for j in range(n):
        if visit[i][j] == -1:
            dfs(i, j)

print(res)