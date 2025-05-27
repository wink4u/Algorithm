import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(list(i for i in range(10)))
cnt = 0
while q:
    now = q.popleft()
    cnt += 1
    if cnt == n:
        print(now)
        exit()

    for i in range(10):
        k = now % 10

        if k > i:
            q.append(now * 10 + i)

print(-1)