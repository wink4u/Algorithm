import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visit = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1

q = deque()
q.append((0, 0, 0, 1))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def res():
    while q:
        x, y, cost, dist = q.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == '0':
                    if not visit[nx][ny][cost]:
                        visit[nx][ny][cost] = 1
                        q.append((nx, ny, cost, dist + 1))
                else:
                    if cost < k and not visit[nx][ny][cost + 1]:
                        visit[nx][ny][cost + 1] = 1
                        q.append((nx, ny, cost + 1, dist + 1))

    return -1

print(res())