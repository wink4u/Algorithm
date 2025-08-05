import sys
from collections import defaultdict
input = sys.stdin.readline

num = defaultdict(int)
poketmon = defaultdict(str)

n, m = map(int, input().split())

for i in range(1, n + 1):
    p = input().strip()
    num[p] = i
    poketmon[str(i)] = p

for _ in range(m):
    k = input().strip()
    if k.isdigit():
        print(poketmon[k])
    else:
        print(num[k])
