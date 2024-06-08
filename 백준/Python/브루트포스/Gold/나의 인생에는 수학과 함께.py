import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(input().split()) for _ in range(N)]

dx = [1, 0]
dy = [0, 1]

visit = [[0 for _ in range(N)] for _ in range(N)]
_max, _min = -1e10, 1e10

def check(x, y, arr, visited):
    global _max, _min

    if x == N - 1 and y == N - 1:
        res = int(arr[0])
        tmp = ''
        for i in range(1, len(arr)):
            if arr[i].isdigit():
                if tmp == '+':
                    res += int(arr[i])
                elif tmp == '-':
                    res -= int(arr[i])
                else:
                    res *= int(arr[i])
            else:
                tmp = arr[i]

        _max = max(_max, res)
        _min = min(_min, res)

    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            arr.append(board[nx][ny])
            visited[nx][ny] = 1
            check(nx, ny, arr, visited)
            visited[nx][ny] = 0
            arr.pop()

check(0, 0, [board[0][0]], visit)
print(_max, _min)