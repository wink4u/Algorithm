import sys
import heapq
input = sys.stdin.readline

n = int(input())
water = [0] + list(map(int, input().split()))
m = int(input())
node = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    node[a].append((b, w))
    node[b].append((a, w))

s, t = map(int, input().split())

q = []
heapq.heappush(q, [0, s, water[s]])
D = [[1e12, 0] for _ in range(n + 1)]
D[s] = [0, water[s]]

ans = 0

while q:
    dist, now, value = heapq.heappop(q)

    if D[now][0] < dist or (D[now][0] == dist and D[now][1] > value):
        continue

    for (nxt, cost) in node[now]:
        nxt_v = dist + cost
        nxt_w = value + water[nxt]

        if D[nxt][0] > nxt_v:
            D[nxt] = [nxt_v, nxt_w]
            heapq.heappush(q, [nxt_v, nxt, nxt_w])
        elif D[nxt][0] == nxt_v:
            if D[nxt][1] < nxt_w:
                D[nxt][1] = nxt_w
                heapq.heappush(q, [nxt_v, nxt, nxt_w])

if D[t][0] == 1e12:
    print(-1)
else:
    print(*D[t])
