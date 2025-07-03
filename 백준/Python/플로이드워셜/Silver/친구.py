import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
friends = [list(input().strip()) for _ in range(n)]
visit = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if friends[i][j] == 'Y' or (friends[i][k] == 'Y' and friends[k][j] == 'Y'):
                visit[i][j] = 1

ans = 0

for v in visit:
    ans = max(ans, sum(v))

print(ans)
