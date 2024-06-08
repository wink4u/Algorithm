import sys
from collections import deque
import copy

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [list(input().strip()) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
copy_arr = copy.deepcopy(arr)

def bfs(i, j, vc):
    q = deque()
    q.append((i, j))
    visit[i][j] = vc
    temp = [[i, j]]
    cnt = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                if arr[nx][ny] == '0':
                    cnt += 1
                    visit[nx][ny] = vc
                    q.append((nx, ny))
                    temp.append((nx, ny))

    for x, y in temp:
        copy_arr[x][y] = cnt

visit_cnt = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            res = 1
            value = []

            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]

                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '0':
                    if copy_arr[nx][ny] == '0':
                        bfs(nx, ny, visit_cnt)
                        visit_cnt += 1

                    if visit[nx][ny] not in value:
                        value.append((visit[nx][ny]))
                        res += copy_arr[nx][ny]

            arr[i][j] = res % 10

for i in range(len(arr)):
    print(''.join(map(str, arr[i])))