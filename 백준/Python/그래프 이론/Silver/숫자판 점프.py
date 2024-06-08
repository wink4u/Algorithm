import sys
input = sys.stdin.readline

res = []

board = [list(input().split()) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y, value, cnt):
    global res
    if cnt == 5:
        if value not in res:
            res.append(value)

        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < 5 and 0 <= ny < 5:
            check(nx, ny, value + board[nx][ny], cnt + 1)

for i in range(5):
    for j in range(5):
        tmp = board[i][j]
        check(i, j, tmp, 0)

print(len(res))