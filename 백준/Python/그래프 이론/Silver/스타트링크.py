import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

q = deque()
q.append(s)
v = [1e8] * (f + 1)
v[s] = 0

while q:
    now = q.popleft()

    if now == g:
        break

    for i in range(2):
        if i == 0:
            nxt = now + u
        else:
            nxt = now - d

        if 1 <= nxt <= f:
            if v[nxt] > v[now] + 1:
                v[nxt] = v[now] + 1
                q.append(nxt)


print('use the stairs' if v[g] == 1e8 else v[g])