import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
check = defaultdict(bool)

for _ in range(n):
    s = input().strip()
    check[s] = True

res = n
for _ in range(m):
    arr = list(input().strip().split(','))

    for a in arr:
        if check[a]:
            check[a] = False
            res -= 1

    print(res)
