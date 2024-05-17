import heapq

inf = 1e10


def solution(n, edge):
    answer = 0

    node = [[] for _ in range(n + 1)]

    for s, e in edge:
        node[s].append((e, 1))
        node[e].append((s, 1))

    def djkstra(start):
        q = []
        D = [inf] * (n + 1)
        D[start] = 0
        heapq.heappush(q, [0, start])

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

    res = djkstra(1)

    _max = max(res[1:])
    return res.count(_max)