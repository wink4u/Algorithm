import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

num = [i for i in range(1, N + 1)]

q = deque(num)
res = []
while q:
    for _ in range(K - 1):
        q.append(q.popleft())
    res.append(q.popleft())


print("<",", ".join(map(str, res)),">", sep='')
