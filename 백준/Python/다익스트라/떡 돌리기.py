import sys
import heapq

input = sys.stdin.readline

n, m, x, y = map(int, input().split())
node = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    node[a].append((b, c * 2))
    node[b].append((a, c * 2))


def djkstra(num):
    D = [1e14] * n
    D[num] = 0

    q = []
    heapq.heappush(q, [0, num])

    while q:
        cost, now = heapq.heappop(q)

        if D[now] < cost:
            continue

        for nxt, value in node[now]:
            if D[nxt] > cost + value:
                D[nxt] = cost + value
                heapq.heappush(q, [cost + value, nxt])

    D.sort()
    res = 0
    cnt = 0
    if D[-1] > x:
        return -1
    for i in range(n):
        if cnt + D[i] > x:
            cnt = D[i]
            res += 1
        else:
            cnt += D[i]

    return res + 1


print(djkstra(y))