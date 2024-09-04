import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())

boss = [[] for _ in range(n + 1)]
c = defaultdict(int)
arr = list(map(int, input().split()))
for i in range(n):
    if arr[i] == -1:
        pass
    else:
        boss[arr[i]].append(i + 1)

for _ in range(m):
    i, w = map(int, input().split())
    c[i] += w


c_items = list(c.items())
ans = [0] * (n + 1)

def bfs(t, w):
    if boss[t]:
        q = deque()
        q.append(t)
        ans[t] += w
        while q:
            child = q.popleft()

            for n_child in boss[child]:
                ans[n_child] += w
                if boss[n_child]:
                   q.append(n_child)
    else:
        ans[t] += w


for r, t in c_items:
    bfs(r, t)

print(*ans[1:])