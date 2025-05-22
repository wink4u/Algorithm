import sys
from collections import defaultdict
input = sys.stdin.readline

n, q = map(int, input().split())
row, col = defaultdict(int), defaultdict(int)
g_max, s_max = 0, 0
gcnt, scnt = 0, 0

for _ in range(q):
    t, a = map(int, input().split())

    if t == 1:
        row[a] += 1
        if row[a] > g_max:
            g_max = row[a]
            gcnt = 1
        elif row[a] == g_max:
            gcnt += 1
    else:
        col[a] += 1
        if col[a] > s_max:
            s_max = col[a]
            scnt = 1
        elif col[a] == s_max:
            scnt += 1

    if gcnt and scnt:
        print(gcnt * scnt)
    elif gcnt:
        print(gcnt * n)
    else:
        print(scnt * n)
