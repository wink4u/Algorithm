import sys
from collections import deque
input = sys.stdin.readline

t, a, b = map(int, input().split())
res = 0

dp = [[0, 0] for _ in range(t + 1)]
q = deque()
q.append((0, 0))

while q:
    now, water = q.popleft()
    res = max(res, now)

    for fruit in [a, b]:
        nxt = fruit + now

        if nxt <= t and not dp[nxt][water]:
            dp[nxt][water] = 1
            q.append((nxt, water))

    if not water:
        nxt = now // 2
        if not dp[nxt][1]:
            dp[nxt][1] = 1
            q.append((nxt, 1))

print(res)