import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
map_v = []

water = deque()
animal = deque()

w_visit = [[0] * C for _ in range(R)]
a_visit = [[0] * C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 비어있는곳 . , 물이 차있는 지역 *, 돌 X, 비버의 굴 D, 고슴도치의 위치 'S'
for i in range(R):
    temp = list(input().rstrip())
    for j in range(C):
        if temp[j] == 'S':
            animal.append((i, j))
            a_visit[i][j] = 1
        elif temp[j] == '*':
            water.append((i, j))
            w_visit[i][j] = 1

    map_v.append(temp)

def water_bfs():
    for _ in range(len(water)):
        x, y = water.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < R and 0 <= ny < C and (map_v[nx][ny] == 'S' or map_v[nx][ny] == '.') and not w_visit[nx][ny]:
                w_visit[nx][ny] = 1
                map_v[nx][ny] = '*'
                water.append((nx, ny))


def animal_bfs():
    cnt = 0
    while animal:

        water_bfs()
        for _ in range(len(animal)):
            x, y = animal.popleft()
            if map_v[x][y] == 'D':
                return cnt

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < R and 0 <= ny < C  and not a_visit[nx][ny]:
                    if map_v[nx][ny] == '.':
                        a_visit[nx][ny] = 1
                        map_v[nx][ny] = 'S'
                        animal.append((nx, ny))
                    elif map_v[nx][ny] == 'D':
                        animal.append((nx, ny))
        cnt += 1

answer = animal_bfs()
if answer == None:
    print('KAKTUS')
else:
    print(answer)