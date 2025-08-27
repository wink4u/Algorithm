import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

q = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[0] * m for _ in range(n)]

for i in range(n):
    if i == 0 or i == n - 1:
        for j in range(m):
            visit[i][j] = 1
            heapq.heappush(q, (-arr[i][j], i, j))
    else:
        visit[i][0] = 1
        heapq.heappush(q, (-arr[i][0], i, 0))

        if m != 1:
            visit[i][m - 1] = 1
            heapq.heappush(q, (-arr[i][m - 1], i, m - 1))

cnt = 0
while q:
    value, x, y = heapq.heappop(q)
    print(x + 1, y + 1)
    cnt += 1

    if cnt == k:
        break

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            visit[nx][ny] = 1
            heapq.heappush(q, (-arr[nx][ny], nx, ny))

