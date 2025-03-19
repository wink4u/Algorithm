import sys
from collections import deque
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
dish = [int(input()) for _ in range(n)]
q = deque(dish[:k])
answer = 0

for i in range(n):
    q.popleft()
    q.append(dish[(i + k) % n])
    answer = max(answer, len(set(list(q) + [c])))

print(answer)