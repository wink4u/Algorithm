from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
blocks = [list(input().strip()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

obstacle = []
def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and blocks[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

    obstacle.append(cnt)

for i in range(N):
    for j in range(N):
        if blocks[i][j] == '1' and not visited[i][j]:
            bfs(i, j)
            
obstacle.sort()
print(len(obstacle))
for count in obstacle:
    print(count)