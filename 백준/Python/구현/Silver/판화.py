import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
command = list(input().strip())
board = [['.'] * n for _ in range(n)]
x, y = 0, 0

check = {'D' : 1, 'U' : 0, 'L' : 2, 'R': 3}
for c in command:
    d = check[c]

    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        if d == 0 or d == 1:
            if board[x][y] == '.':
                board[x][y] = '|'
            elif board[x][y] == '-':
                board[x][y] = '+'
        else:
            if board[x][y] == '.':
                board[x][y] = '-'
            elif board[x][y] == '|':
                board[x][y] = '+'

        if d == 0 or d == 1:
            if board[nx][ny] == '.':
                board[nx][ny] = '|'
            elif board[nx][ny] == '-':
                board[nx][ny] = '+'
        else:
            if board[nx][ny] == '.':
                board[nx][ny] = '-'
            elif board[nx][ny] == '|':
                board[nx][ny] = '+'

        x, y = nx, ny

for i in range(n):
    print(''.join(board[i]))