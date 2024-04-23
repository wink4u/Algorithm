import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

board = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs1(visit, sx, sy, value):
    q = deque()
    q.append((sx, sy))
    visit[sx][sy] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == value:
                if not visit[nx][ny]:
                    q.append((nx, ny))
                    visit[nx][ny] = 1

    return visit


def bfs2(visit, sx, sy, value):
    q = deque()
    q.append((sx, sy))
    visit[sx][sy] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if value == 'B':
                    if value == board[nx][ny]:
                        q.append((nx, ny))
                        visit[nx][ny] = 1
                else:
                    if board[nx][ny] != 'B':
                        q.append((nx, ny))
                        visit[nx][ny] = 1

    return visit


visit_1 = [[0 for _ in range(N)] for _ in range(N)]
visit_2 = [[0 for _ in range(N)] for _ in range(N)]

cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if not visit_1[i][j]:
            visit_1 = bfs1(visit_1, i, j, board[i][j])
            cnt1 += 1

        if not visit_2[i][j]:
            visit_2 = bfs2(visit_2, i, j, board[i][j])
            cnt2 += 1

print(cnt1, cnt2)
