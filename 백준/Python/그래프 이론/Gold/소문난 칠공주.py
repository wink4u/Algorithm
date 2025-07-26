import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

arr = [list(input().strip()) for _ in range(5)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

graph = [(i // 5, i % 5) for i in range(25)]
comb = list(combinations(range(25), 7))

res = 0
for com in comb:
    tmp = [graph[i] for i in com]
    cnt = sum(1 for x, y in tmp if arr[x][y] == 'S')

    if cnt < 4:
        continue

    q = deque()
    q.append(tmp[0])
    visit = set()
    visit.add(tmp[0])
    # print(tmp[0])

    total = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (nx, ny) in tmp and (nx, ny) not in visit:
                visit.add((nx, ny))
                q.append((nx, ny))
                total += 1

    if total == 7:
        res += 1

print(res)