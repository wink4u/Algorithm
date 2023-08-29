import sys
from collections import deque


input = sys.stdin.readline

N, L, R = map(int, input().split())

map_v = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sx = sy = 0

def bfs():
    q = deque()
    q.append((0, 0, map_v[0][0]))