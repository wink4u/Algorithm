import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline

N, L, R = map(int, input().split())

map_v = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sx = sy = 0

def bfs():
    q = deque()
    q.append((sx, sy))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[sx][sy] = 1

    change = []
    change_value = []
    while q:
        x, y = q.popleft()

        change_cnt = 0

        flag = 0

        if (x, y) not in change:
            change.append((x, y))
            change_value.append(map_v[x][y])
            flag = 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                res = map_v[nx][ny] - map_v[x][y]
                print(res, x, y, nx, ny)
                if L <= abs(res) <= R:
                    print(nx, ny)
                    if (nx, ny) not in change:
                        change.append((nx, ny))
                        change_value.append(map_v[nx][ny])
                        change_cnt += 1

                q.append((nx, ny))
                visited[nx][ny] = 1

        if change_cnt == 0:
            if flag == 1:
                change.pop()
                change_value.pop()


    if change:
        div = sum(change_value) // len(change)
        for i in range(len(change)):
            tx, ty = change[i]
            map_v[tx][ty] = div

        print(change)
        pprint(map_v)
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


