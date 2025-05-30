import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
node = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

q = deque()
q.append(1)
d = [1e9] * (n + 1)
d[1] = 0
distance = 0

res = set()

while q:
    now = q.popleft()

    for nxt in node[now]:
        if d[nxt] > d[now] + 1:
            d[nxt] = d[now] + 1
            q.append(nxt)

            if d[nxt] > distance:
                distance = d[nxt]
                res = {nxt}
            elif d[nxt] == distance:
                res.add(nxt)

        elif d[nxt] == distance:
            res.add(nxt)

res = list(res)
res.sort()
print(res[0], distance, len(res))
