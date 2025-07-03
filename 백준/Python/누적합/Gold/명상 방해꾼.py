import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
birds = []

for _ in range(n):
    direction, s = input().split()
    birds.append((direction, list(map(int, s))))

value = [0] * m

for side, bird in birds:
    for i in range(m):
        if bird[i]:
            value[i] += -1 if side == 'L' else 1

_min = 1e11
idx = 0

for i in range(n):
    tmp = value[:]
    side, bird = birds[i]

    for j in range(m):
        if bird[j]:
            tmp[j] -= -1 if side == 'L' else 1

    v = 0
    _max = 0

    for t in tmp:
        v += t
        _max = max(_max, abs(v))

    if _max < _min:
        _min = _max
        idx = i + 1

print(idx)
print(_min)