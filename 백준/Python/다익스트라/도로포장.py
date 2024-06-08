import sys
import heapq

input = sys.stdin.readline

INF = 1e8

# 도시의 수 N, 도로의 수 M, 포장할 도로의 수 K
N, M, K = map(int, input().split())

node = [[] for _ in range(N + 1)]

for i in range(M):
    s, e, w = map(int, input().split())
    node[s].append([e, w])
    node[e].append([s, w])

D = [[INF for _ in range(K + 1)] for _ in range(N + 1)]

def djkstra(start):
    cnt = 0
    D[start][cnt] = 0
    q = []
    heapq.heappush(q, [0, start, cnt])

    while q:
        dist, now, cnt = heapq.heappop(q)

        if dist > D[now][cnt]:
            continue

        for i in node[now]:
            cost = dist + i[1]
            if cost < D[i[0]][cnt]:
                D[i[0]][cnt] = cost
                heapq.heappush(q, [cost, i[0], cnt])

            if cnt < K and D[i[0]][cnt + 1] > dist:
                D[i[0]][cnt + 1] = dist
                heapq.heappush(q, [dist, i[0], cnt + 1])

djkstra(1)
print(min(D[N]))