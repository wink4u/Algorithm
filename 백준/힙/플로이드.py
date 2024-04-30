import sys
import heapq
input = sys.stdin.readline

N = int(input())

node = [[] for _ in range(N + 1)]

m = int(input())

for _ in range(m):
    s, e, v = map(int, input().split())
    node[s].append([e, v])

inf = 1e11

def djkstra(s):
    q = []
    D = [inf] * (N + 1)
    D[s] = 0
    heapq.heappush(q, [0, s])

    while q:
        dist, now = heapq.heappop(q)

        if dist > D[now]:
            continue

        for e, value in node[now]:
            cost = D[now] + value

            if cost < D[e]:
                D[e] = cost
                heapq.heappush(q, [cost, e])

    for i in range(1, len(D)):
        if D[i] == inf:
            D[i] = 0

    return D[1:]

for i in range(1, N + 1):
    print(*djkstra(i))
