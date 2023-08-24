import sys
from collections import deque

sys.setrecursionlimit(50000000)
input = sys.stdin.readline

A, B, N, M = map(int, input().split())

visited = [0] * 100001
doldari = [0] * 100001

dx = [1, -1, A, -A, B, -B, A, B]

def check(sx):
    q = deque()
    q.append((sx))
    visited[sx] = 1

    while q:
        x = q.popleft()

        for i in range(8):

            if i <= 5:
                nx = x + dx[i]

                if 0 <= nx <= 100000 and not visited[nx]:
                    visited[nx] = 1
                    doldari[nx] = doldari[x] + 1
                    q.append((nx))

            else:
                nx = x * dx[i]

                if 0 <= nx <= 100000 and not visited[nx]:
                    visited[nx] = 1
                    doldari[nx] = doldari[x] + 1
                    q.append((nx))

check(N)

print(doldari[M])