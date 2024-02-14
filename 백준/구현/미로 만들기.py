import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

sx, sy = 50, 50

map_v = [[0 for _ in range(101)] for _ in range(101)]

map_v[sx][sy] = '.'

N = int(input())

command = list(input().strip())

d = 0

min_x, min_y, max_x, max_y = sx, sy, sx, sy

for i in range(N):
    if command[i] == 'F':
        nx = sx + dx[d]
        ny = sy + dy[d]
        map_v[nx][ny] = '.'
        min_x = min(min_x, nx)
        max_x = max(max_x, nx)
        min_y = min(min_y, ny)
        max_y = max(max_y, ny)

        sx, sy = nx, ny
    else:
        if command[i] == 'L':
            d -= 1
            if d < 0:
                d = 3
        else:
            d += 1
            if d > 3:
                d = 0

for i in range(min_x, max_x + 1):
    temp = map_v[i][min_y : max_y + 1]
    for j in range(len(temp)):
        if temp[j] == 0:
            temp[j] = '#'

    print(''.join(map(str, temp)))