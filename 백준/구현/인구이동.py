import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())

map_v = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]

    flag = 0

    for i in range(N):
        for j in range(N):

            if visited[i][j] == 0:
                change = []
                q.append((i, j))
                change.append((i, j))
                visited[i][j] = 1

                while q:
                    x, y = q.popleft()

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            res = map_v[nx][ny] - map_v[x][y]
                            if L <= abs(res) <= R:
                                visited[nx][ny] = 1
                                change.append((nx, ny))
                                q.append((nx, ny))

                if len(change) > 1:
                    flag = 1
                    div = 0

                    for cx, cy in change:
                        div += map_v[cx][cy]

                    div //= len(change)

                    for cx, cy in change:
                        map_v[cx][cy] = div

    if flag:
        return 0
    else:
        return 1

ans = 0
while True:
    bfs_res = bfs()

    if bfs_res:
        break

    ans += 1

print(ans)