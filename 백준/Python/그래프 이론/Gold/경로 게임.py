import sys
from collections import deque
input = sys.stdin.readline

m = int(input())
board = [list(input().strip()) for _ in range(2)]

dx = [0, -1, 1]
dy = [1, 0, 0]

res = 0

for k in range(2):
    if board[k][0] == '.':
        visit = [[-1] * m for _ in range(2)]
        visit[k][0] = 0
        q = deque()
        q.append((k, 0))

        while q:
            x, y = q.popleft()

            for d in range(3):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < 2 and 0 <= ny < m and visit[x][y] > visit[nx][ny]:
                    if board[nx][ny] == '.':
                        flag = 0

                        if d == 0:
                            if x == 0 and board[x + 1][y] == '.' and visit[x][y] > visit[x + 1][y]:
                                # print(x, y, nx, ny, visit[x][y], visit[x+1][y])
                                flag = 1
                            elif x == 1 and board[x - 1][y] == '.' and visit[x][y] > visit[x - 1][y]:
                                # print(x, y, nx, ny, visit[x][y], visit[x - 1][y])
                                flag = 1

                        if flag:
                            visit[nx][ny] = visit[x][y] + 1
                        else:
                            visit[nx][ny] = visit[x][y]

                        q.append((nx, ny))

        if board[0][-1] == '.' and board[1][-1] == '.':
            visit[0][-1] += 1
            visit[1][-1] += 1

        res = max(res, visit[0][-1], visit[1][-1])

print(res)
