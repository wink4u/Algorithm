import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
sx, sy = map(int, input().split())

res = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt, apple):
    global res

    if cnt > 3:
        return

    if apple >= 2:
        res = 1
        return

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] != -1:
            temp = board[x][y]
            board[x][y] = -1
            dfs(nx, ny, cnt + 1, apple + (board[nx][ny] == 1))
            board[x][y] = temp


dfs(sx, sy, 0, 0)

print(res)
