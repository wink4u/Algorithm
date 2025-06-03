import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
q = deque()
q.append(n)

for i in range(n - 1, 0, -1):
    q.appendleft(i)
    for j in range(i):
        q.appendleft(q.pop())

ans = list(q)
print(*ans)