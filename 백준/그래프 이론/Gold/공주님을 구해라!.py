import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
maps = []
kx, ky = 0, 0
for i in range(N):
    tmp = list(map(int, input().split()))

    if 2 in tmp:
        kx, ky = i, tmp.index(2)

    maps.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, mx, my):
    q = deque()
    q.append((sx, sy, 0))
    visit = [[0 for _ in range(M)] for _ in range(N)]

    while q:
        x, y, time = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 1 and not visit[nx][ny]:
                if nx == mx and ny == my:
                    return time + 1
                visit[nx][ny] = 1
                q.append((nx, ny, time + 1))

    return 1e10

normal = bfs(0, 0, N - 1, M - 1)
knife = bfs(0, 0, kx, ky)

if knife != 1e10:
    use_knife = knife + abs(N - 1 - kx) + abs(M - 1 - ky)
else:
    use_knife = knife

ans = min(use_knife, normal)
print(ans if ans <= T else 'Fail')