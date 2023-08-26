import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

map_v = []
birus = []

visit = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    temp = list(map(int, input().split()))
    print(temp)
    for j in range(M):
        if temp[j] == 2:
            birus.append((i, j))
            visit[i][j] = 1

    map_v.append(temp)

