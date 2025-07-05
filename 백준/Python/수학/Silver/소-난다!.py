import sys
from itertools import combinations
import math
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
combi = list(combinations(arr, m))
res = set()

for c in combi:
    cs = sum(c)
    if cs not in res:
        flag = 0

        for j in range(2, int(math.sqrt(cs)) + 1):
            if cs % j == 0:
                flag = 1
                break

        if not flag:
            res.add(cs)

res = list(res)

if res:
    res.sort()
    print(*res)
else:
    print(-1)