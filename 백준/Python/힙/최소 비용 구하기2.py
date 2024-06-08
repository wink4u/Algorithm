import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
E = int(input())

bus = defaultdict(list)

inf = int(1e10)
D = [inf] * (N + 1)

for _ in range(E):
    s, e, w = map(int, input().split())
    bus[s].append([e, w])

start, end = map(int, input().split())

prev = [0] * (N + 1)

def djkstra(st):
    q = []

    D[st] = 0
    heapq.heappush(q, (0, st))

    while q:
        dist, now = heapq.heappop(q)

        if dist > D[now]:
            continue

        for e, value in bus[now]:
            cost = D[now] + value

            if cost < D[e]:
                prev[e] = now
                D[e] = cost
                heapq.heappush(q, [cost, e])

djkstra(start)
print(D[end])

path = [end]
now = end
while now != start:
    now = prev[now]
    path.append(now)

print(len(path))

path.reverse()

print(*path)