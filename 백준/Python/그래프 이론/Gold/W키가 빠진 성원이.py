import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []
sx, sy = 0, 0
for i in range(n):
    tmp = list(input().strip())
    if 'F' in tmp:
        sx, sy = i, tmp.index('F')

    arr.append(tmp)

q = deque()
q.append((sx, sy))

dx = [-1, 0, 0, -1, -1, 1, 1]
dy = [0, -1, 1, -1, 1, -1, 1]

visit = [[0] * n for _ in range(n)]
visit[sx][sy] = 1

res = 0

while q:
    x, y = q.popleft()

    for d in range(7):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == '.':
            if not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx, ny))
                res += 1

print(res)
