import sys
from collections import deque
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input())
node = [[] for _ in range(n + 1)]

for _ in range(n):
    a, b = map(int, input().split())

    node[a].append(b)
    node[b].append(a)

visit = [-1] * (n + 1)
route = set()
flag = 0


def dfs(start, now, cnt, arr):
    global route, flag

    for nxt in node[now]:
        if nxt == start and cnt > 2:
            for r in arr:
                route.add(r)
            flag = 1

        if visit[nxt] == -1:
            visit[nxt] = 1
            arr.append(nxt)
            dfs(start, nxt, cnt + 1, arr)
            visit[nxt] = -1
            arr.pop()



for i in range(1, n + 1):
    if flag:
        break

    visit[i] = 1
    dfs(i, i, 1, [i])
    visit[i] = -1

q = deque()

for r in route:
    q.append((0, r))
    visit[r] = 0

while q:
    cnt, now = q.popleft()

    for nxt in node[now]:
        if visit[nxt] == -1:
            visit[nxt] = cnt + 1
            q.append((cnt + 1, nxt))

print(*visit[1:])