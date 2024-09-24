import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

node = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    node[a].append([b, c])
    node[b].append([a, c])


def bfs(s, e, mid, v):
    v[s] = 1
    q = deque()
    q.append(s)

    while q:
        now = q.popleft()
        if now == e:
            return True

        for nx, nc in node[now]:
            if not v[nx] and mid <= nc:
                q.append(nx)
                v[nx] = 1

    return False

start, end = map(int, input().split())
left, right = 1, 1000000000

while left <= right:
    visit = [0 for _ in range(N + 1)]
    mid = (left + right) // 2

    if bfs(start, end, mid, visit):
        left = mid + 1
    else:
        right = mid - 1

print(right)