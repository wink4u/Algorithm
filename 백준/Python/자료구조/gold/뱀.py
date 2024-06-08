import sys
from collections import deque
input = sys.stdin.readline


dx = [-1, 0, 1, 0] # 상 좌 하 우
dy = [0, -1, 0, 1]

# 보드의 크기
N = int(input())

# 맵의 크기
map_v = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 사과의 개수
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    map_v[x][y] = 1

# 뱀의 위치 바꿔주는 커맨드
L = int(input())

command = deque()
for _ in range(L):
    command.append(list(input().split()))

start = 3

snake = deque()

time, com = command.popleft()
time = int(time)

# 뱀의 시작 위치 및 시간
sx, sy = 1, 1
cnt = 0
snake.append((sx, sy))
while True:
    nx = sx + dx[start]
    ny = sy + dy[start]

    if 1 <= nx < N + 1 and 1 <= ny < N + 1 and (nx, ny) not in snake:
        snake.append((nx, ny))
        if map_v[nx][ny] == 0:
            snake.popleft()

        elif map_v[nx][ny] == 1:
            map_v[nx][ny] = 0
        sx = nx
        sy = ny
        cnt += 1

    else:
        cnt += 1
        break

    if cnt == time:
        if com == 'L':
            start += 1
            if start == 4:
                start = 0
        elif com == 'D':
            start -= 1
            if start == -1:
                start = 3

        if command:
            time, com = command.popleft()
            time = int(time)

print(cnt)