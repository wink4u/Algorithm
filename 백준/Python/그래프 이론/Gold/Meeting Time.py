import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

bessi = [[] for _ in range(n + 1)]
elssi = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, v, w = map(int, input().split())
    bessi[a].append([b, v])
    elssi[a].append([b, w])

def bfs():
    q = deque()
    q.append((1, 0))
    visited = [set() for _ in range(n + 1)]
    visited[1].add(0)
    res = set()

    while q:
        now, cost = q.popleft()
        if now == n:
            res.add(cost)
            continue

        for nxt, value in bessi[now]:
            next_cost = cost + value
            if next_cost not in visited[nxt]:
                visited[nxt].add(next_cost)
                q.append((nxt, next_cost))

    return res


ans1 = list(bfs())

def bfs2():
    q = deque()
    q.append((1, 0))
    visited = [set() for _ in range(n + 1)]
    visited[1].add(0)
    res = 1e9

    while q:
        now, cost = q.popleft()
        if now == n:
            if cost in ans1:
                res = min(res, cost)
            continue

        for nxt, value in elssi[now]:
            next_cost = cost + value
            if next_cost not in visited[nxt]:
                visited[nxt].add(next_cost)
                q.append((nxt, next_cost))

    return res


result = bfs2()

if result == 1e9:
    print('IMPOSSIBLE')
else:
    print(result)