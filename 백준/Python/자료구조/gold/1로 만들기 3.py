import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
visit = set()
q = deque()
q.append((n, 0))
visit.add(n)

while q:
    now, cnt = q.popleft()
    if now == 1:
        print(cnt)
        break

    if now % 3 == 0 and (now // 3) not in visit:
        visit.add(now // 3)
        q.append((now // 3, cnt + 1))

    if now % 2 == 0 and (now // 2) not in visit:
        visit.add(now // 2)
        q.append((now // 2, cnt + 1))

    if now - 1 not in visit:
        visit.add(now - 1)
        q.append((now - 1, cnt + 1))