import sys
import heapq
input = sys.stdin.readline

inf = int(1e7)

V, E = map(int, input().split())

start = int(input())
node = [[] for _ in range(V+1)]
nodes = [[] * (V + 1)]

for i in range(E):
    s, e, w = map(int, input().split())
    node[s].append((e, w))

D = [inf] * (V + 1)

def djkstra(num):
    q = []
    D[num] = 0
    heapq.heappush(q, [0, num])

    while q:
        dist, now = heapq.heappop(q)

        if dist > D[now]:
            continue

        for i in node[now]:
            cost = dist + i[1]

            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

    return D

ans = djkstra(start)

for i in range(1, len(ans)):
    if ans[i] == inf:
        print('INF')
    else:
        print(ans[i])