import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    arr = [0, 0] + arr
elif n == 2:
    arr = [0] + arr

inf = 1e8

DP = [[[inf] * 61 for _ in range(61)] for _ in range(61)]
DP[arr[0]][arr[1]][arr[2]] = 0

q = deque()
q.append((arr[0], arr[1], arr[2]))
v = [[9, 3, 1], [9, 1, 3], [3, 1, 9], [3, 9, 1], [1, 3, 9], [1, 9, 3]]

while q:
    a, b, c = q.popleft()

    for i in range(6):
        na, nb, nc = max(a - v[i][0], 0), max(b - v[i][1], 0), max(c - v[i][2], 0)
        if DP[na][nb][nc] > DP[a][b][c] + 1:
            DP[na][nb][nc] = DP[a][b][c] + 1
            q.append((na, nb, nc))

print(DP[0][0][0])