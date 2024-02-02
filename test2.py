import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
value = int(input())

start = 1

arr = [[0 for _ in range(N)] for _ in range(N)]

x, y = N // 2, N // 2
d = 0

arr[x][y] = start

while True:
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < N and 0 <= ny < N and not arr[nx][ny]:
        start += 1
        arr[nx][ny] = start
        nx, ny = x, y