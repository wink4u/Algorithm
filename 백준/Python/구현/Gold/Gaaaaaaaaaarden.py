import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m, g, r = map(int, input().split())
board = []
can = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 2:
            can.append((i, j))
    board.append(tmp)


check = list(combinations(can, g))

def pick(arr, idx):
    global red

    if len(arr) == r:
        t = sorted(arr)
        if t not in red:
            red.append(t)
        return

    for i in range(idx, len(can)):
        if can[i] not in green and can[i] not in arr:
            arr.append(can[i])
            pick(arr, idx + 1)
            arr.pop()


res = 0

def bfs(gr, rd):
    global res
    v = [[[0, 0] for _ in range(m)] for _ in range(n)]
    for x, y in gr:
        v[x][y][0] = 1

    for x, y in rd:
        v[x][y][1] = 1

    gq = deque(gr)
    rq = deque(rd)

    cnt = 0
    c = 2

    while gq or rq:
        for _ in range(len(gq)):
            gx, gy = gq.popleft()

            if v[gx][gy][0] == v[gx][gy][1] == c - 1:
                continue

            for d in range(4):
                nx = gx + dx[d]
                ny = gy + dy[d]

                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] != 0 and v[nx][ny][0] == 0 and v[nx][ny][1] == 0:
                        v[nx][ny][0] = c
                        gq.append((nx, ny))

        for _ in range(len(rq)):
            rx, ry = rq.popleft()

            for d in range(4):
                nx = rx + dx[d]
                ny = ry + dy[d]

                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] != 0:
                        if v[nx][ny][0] == c:
                            if v[nx][ny][1] == 0:
                                cnt += 1
                                v[nx][ny][1] = c
                        elif v[nx][ny][0] == 0 and v[nx][ny][1] == 0:
                            v[nx][ny][1] = c
                            rq.append((nx, ny))

        c += 1
    res = max(res, cnt)


for i in range(len(check)):
    green = check[i]
    red = []
    pick([], 0)
    for j in range(len(red)):
        bfs(green, red[j])

print(res)