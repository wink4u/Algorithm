import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(input().split())
ans = sorted(arr)

res = 1e8
visit = set()
visit.add(''.join(arr))

q = deque()
q.append((arr, 0))

while q:
    now, cnt = q.popleft()

    if now == ans:
        res = cnt
        break

    for i in range(n - k + 1):
        r = now[i:i + k]
        r.reverse()
        ttmp = now[:i] + r + now[i + k:]
        t_str = ''.join(ttmp)
        if t_str not in visit:
            visit.add(t_str)
            q.append((ttmp, cnt + 1))


print(-1 if res == 1e8 else res)