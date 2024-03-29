from collections import deque
import sys

input = sys.stdin.readline

def bfs(visited):
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if ice[nx][ny] == 1:
                    visited[nx][ny] += 1
                elif visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                ice[i][j] = 0
                
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

ice = [list(map(int, input().split())) for _ in range(N)]

result = 0

while True:
    count = 0
    for i in range(N):
        if sum(ice[i]) == 0:
            count += 1

    if count == N:
        break

    visit = [[0] * M for _ in range(N)]
    bfs(visit)
    result += 1

print(result)