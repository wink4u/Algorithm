import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
cows = defaultdict(int)

for _ in range(N):
    tmp = list(input().split())
    tmp.sort()
    tmp = tuple(tmp)
    if cows[tmp]:
        cows[tmp] += 1
    else:
        cows[tmp] = 1

res = list(cows.items())
res.sort(key = lambda x : -x[1])
print(res[0][1])