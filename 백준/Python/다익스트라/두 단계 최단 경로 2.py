import sys
import heapq
input = sys.stdin.readline

inf = sys.maxsize
n, m = map(int, input().split())
node = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    node[u].append((v, w))
    node[v].append((u, w))


x, z = map(int, input().split())
p = int(input())
arr = list(map(int, input().split()))

def djkstra(num):
    D = [inf] * (n + 1)
    D[num] = 0

    q = []
    heapq.heappush(q, (0, num))

    while q:
        cost, now = heapq.heappop(q)

        if D[now] < cost:
            continue

        for nxt, value in node[now]:
            dist = cost + value

            if D[nxt] > dist:
                D[nxt] = dist
                heapq.heappush(q, (dist, nxt))

    return D


djk_x = djkstra(x)
djk_z = djkstra(z)
res = inf
for y in arr:
    res = min(res, djk_x[y] + djk_z[y])

print(res if res != inf else -1)