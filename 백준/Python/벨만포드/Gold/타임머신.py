import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
inf = float('inf')
nodes = []
D = [inf] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    nodes.append([a, b, c])

def bf(s):
    D[s] = 0

    for i in range(n):
        for j in range(m):
            cur = nodes[j][0]
            nxt = nodes[j][1]
            cost = nodes[j][2]

            if D[cur] != inf and D[nxt] > D[cur] + cost:
                D[nxt] = D[cur] + cost

                if i == n - 1:
                    return True

    return False

check = bf(1)

if check:
    print(-1)
else:
    for i in range(2, n + 1):
        if D[i] == inf:
            print(-1)
        else:
            print(D[i])