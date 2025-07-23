import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]

sx, sy = n - 1, 0
ex, ey = 0, m - 1

visit = [[0] * m for _ in range(n)]
visit[sx][sy] = 1

res = list()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(v, x, y, cnt, tmp):
    global res

    if x == ex and y == ey:
        if cnt == k:
            res.append(tmp[:])
        return

    if cnt > k:
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
            if arr[nx][ny] == '.':
                v[nx][ny] = 1
                tmp.append((nx, ny))
                dfs(v, nx, ny, cnt + 1, tmp)
                tmp.pop()
                v[nx][ny] = 0


dfs(visit, sx, sy, 1, [])
print(len(res))
