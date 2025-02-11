import sys
from collections import deque
input = sys.stdin.readline

n, k, r = map(int, input().split())

bridge = set()
cow = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    bridge.add((r1 - 1, c1 - 1, r2 - 1, c2 - 1))
    bridge.add((r2 - 1, c2 - 1, r1 - 1, c1 - 1))

for _ in range(k):
    cx, cy = map(int, input().split())
    cow.append([cx - 1, cy - 1])


visit = [[-1] * n for _ in range(n)]
group = 0
check = []

for i in range(n):
    for j in range(n):
        if visit[i][j] == -1:
            q = deque()
            q.append((i, j))
            visit[i][j] = group
            cnt = 0

            while q:
                x, y = q.popleft()

                if [x, y] in cow:
                    cnt += 1

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == -1:
                        if (x, y, nx, ny) not in bridge:
                            visit[nx][ny] = group
                            q.append((nx, ny))

            check.append(cnt)
            group += 1

meet_cow = sum((c * (c - 1)) // 2 for c in check if c > 1)
print((k * (k - 1)) // 2 - meet_cow)