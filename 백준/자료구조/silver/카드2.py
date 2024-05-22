import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

cards = [i for i in range(1, N + 1)]
q = deque(cards)

if N == 1:
    print(1)
else:
    while len(q) != 2:
        tmp = q.popleft()
        tmp2 = q.popleft()
        q.append(tmp2)

    print(q[1])
