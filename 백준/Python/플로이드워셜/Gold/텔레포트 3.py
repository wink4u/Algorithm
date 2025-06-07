import sys
from collections import defaultdict
input = sys.stdin.readline

node = defaultdict(list)
result = defaultdict(int)

xs, ys = map(int, input().split())
xe, ye = map(int, input().split())

node[0] = [xs, ys]
node[1] = [xe, ye]

dp = [[1e13] * 8 for _ in range(8)]
dp[0][1] = abs(xs - xe) + abs(ys - ye)

cnt = 2
for _ in range(3):
    a, b, c, d = map(int, input().split())
    dp[cnt][cnt + 1] = 10
    dp[cnt + 1][cnt] = 10
    node[cnt] = [a, b]
    node[cnt + 1] = [c, d]
    cnt += 2

for i in range(8):
    ix, iy = node[i]
    for j in range(8):
        jx, jy = node[j]
        if i != j:
            dp[i][j] = min(dp[i][j], abs(ix - jx) + abs(iy - jy))

for k in range(8):
    for i in range(8):
        for j in range(8):
            if i != j and i != k:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

print(dp[0][1])