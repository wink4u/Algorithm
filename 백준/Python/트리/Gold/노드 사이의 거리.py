import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, d = map(int, input().split())
    tree[a].append([b, d])
    tree[b].append([a, d])


def node_bfs(s, e):
    q = deque()
    q.append((s, 0))
    visit = [0] * (n + 1)
    visit[s] = 1

    while q:
        now, cost = q.popleft()

        for nxt, nxt_cost in tree[now]:
            if not visit[nxt]:
                if nxt == e:
                    return cost + nxt_cost
                visit[nxt] = 1
                q.append((nxt, cost + nxt_cost))


for _ in range(m):
    start, end = map(int, input().split())
    print(node_bfs(start, end))