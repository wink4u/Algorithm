import sys
from collections import deque
input = sys.stdin.readline

n, s = map(int, input().split())
cars = list(map(int, input().split()))
oils = list(map(int, input().split()))

v = [0] * (n)

q = deque()
q.append(s - 1)
v[s - 1] = 1

while q:
    idx = q.popleft()

    for i in range(idx - 1, -1, -1):
        if cars[i] < cars[idx] - oils[idx]:
            break

        if v[i]:
            continue

        q.append(i)
        v[i] = 1

    for i in range(idx + 1, n):
        if cars[i] > cars[idx] + oils[idx]:
            break

        if v[i]:
            continue

        q.append(i)
        v[i] = 1

for i in range(n):
    if v[i]:
        print(i + 1, end = ' ')