import sys
from collections import deque
input = sys.stdin.readline

a, b, c = map(int, input().split())
total = a + b + c

if total % 3 != 0:
    print(0)
    exit()

visit = [[False] * total for _ in range(total)]

q = deque([(a, b)])
visit[a][b] = True

while q:
    a, b = q.popleft()
    c = total - (a + b)

    if a == b == c:
        print(1)
        exit()

    for x, y in [(a, b), (a, c), (b, c)]:
        if x == y:
            continue
        if x > y:
            x, y = y, x

        x, y = x + x, y - x
        _min = min(x, y, total - (x + y))
        _max = max(x, y, total - (x + y))
        if visit[_min][_max]:
            continue

        q.append([_min, _max])
        visit[_min][_max] = True

print(0)
