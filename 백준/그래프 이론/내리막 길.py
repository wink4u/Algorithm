import sys
import heapq

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

map_v = [list(map(int, input().split())) for _ in range(N)]

s_x, s_y = 0, 0
e_x, e_y = N - 1, M - 1

visited = [[0] * M for _ in range(N)]


def check(sx, sy):
    q = []
    heapq.heappush(q, (-map_v[sx][sy], sx, sy))
    visited[sx][sy] = 1

    while q:
        value, x, y = heapq.heappop(q)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and map_v[x][y] > map_v[nx][ny]:
                if not visited[nx][ny]:
                    heapq.heappush(q, (-map_v[nx][ny], nx, ny))

                visited[nx][ny] += visited[x][y]


check(s_x, s_y)
print(visited[e_x][e_y])