import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs_bird():
    while bq:
        x, y = bq.popleft()

        if x == ex and y == ey:
            return True

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and not b_visit[nx][ny]:
                if map_v[nx][ny] == '.':
                    bq.append((nx, ny))
                else:
                    bq_tmp.append((nx, ny))
                b_visit[nx][ny] = 1

    return False


def bfs_wall():
    while wq:
        x, y = wq.popleft()
        if map_v[x][y] == 'X':
            map_v[x][y] = '.'

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and not w_visit[nx][ny]:
                if map_v[nx][ny] == 'X':
                    wq_tmp.append((nx, ny))
                else:
                    wq.append((nx, ny))
                w_visit[nx][ny] = 1


sx, sy, ex, ey = 0, 0, 0, 0

cnt = 0
bq, wq, bq_tmp, wq_tmp = deque(), deque(), deque(), deque()
b_visit = [[0 for _ in range(C)] for _ in range(R)]
w_visit = [[0 for _ in range(C)] for _ in range(R)]

flag = 1
map_v = []
for i in range(R):
    map_v.append(list(input().strip()))
    for j in range(C):
        if map_v[i][j] == '.':
            w_visit[i][j] = 1
            wq.append((i, j))
        elif map_v[i][j] == 'L':
            if flag:
                sx, sy = i, j
                b_visit[i][j] = 1
                flag = 0
            else:
                ex, ey = i, j

            wq.append((i, j))
            map_v[i][j] = '.'

bq.append((sx, sy))

while True:
    bfs_wall()
    if bfs_bird():
        print(cnt)
        break

    cnt += 1
    bq, wq = bq_tmp, wq_tmp
    bq_tmp, wq_tmp = deque(), deque()