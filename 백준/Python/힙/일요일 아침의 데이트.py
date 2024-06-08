import sys
import heapq

input = sys.stdin.readline

# 세로 가로
N, M = map(int, input().split())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = []
garbage = []
sx, sy = 0, 0

for i in range(N):
    tmp = list(input().strip())
    for j in range(M):
        if tmp[j] == 'g':
            garbage.append([i, j])
        elif tmp[j] == 'S':
            sx, sy = i, j

    arr.append(tmp)

for gx, gy in garbage:
    for d in range(4):
        ngx = gx + dx[d]
        ngy = gy + dy[d]
        if 0 <= ngx < N and 0 <= ngy < M and arr[ngx][ngy] == '.':
            arr[ngx][ngy] = '*'


visit = [[0 for _ in range(M)] for _ in range(N)]

res = []

q = []
heapq.heappush(q, (0, 0, sx, sy))
# x, y, 쓰레기, 인근 쓰레기길
visit[sx][sy] = 1

while q:
    gc, ng, x, y = heapq.heappop(q)

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
            visit[nx][ny] = 1
            if arr[nx][ny] == '.':
                heapq.heappush(q, (gc, ng, nx, ny))
            elif arr[nx][ny] == '*':
                heapq.heappush(q, (gc, ng + 1, nx, ny))
            elif arr[nx][ny] == 'g':
                heapq.heappush(q, (gc + 1, ng, nx, ny))
            else:
                print(gc, ng)
                break