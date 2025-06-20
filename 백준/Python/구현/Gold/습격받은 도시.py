import sys
input = sys.stdin.readline

n = int(input())
city = [list(input().strip()) for _ in range(n)]
visit = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if city[i][j] == 'O':
            for d in range(4):
                x, y = i, j
                while True:
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < n and city[nx][ny] == '.':
                        if not visit[nx][ny]:
                            visit[nx][ny] = 1
                    else:
                        break

                    x, y = nx, ny

for i in range(n):
    for j in range(n):
        if not visit[i][j] and city[i][j] == '.':
            city[i][j] = 'B'

for i in range(n):
    print(''.join(city[i]))