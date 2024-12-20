import sys
import heapq
input = sys.stdin.readline

t = int(input())
inf = 1e11

for _ in range(t):
    n, d, c = map(int, input().split())

    node = [[] for _ in range(n + 1)]
    D = [inf] * (n + 1)
    D[c] = 0

    for _ in range(d):
        a, b, s = map(int, input().split())
        node[b].append([a, s])

    q = []
    heapq.heappush(q, [c, 0])

    while q:
        now, cost = heapq.heappop(q)

        if cost > D[now]:
            continue

        for nxt, nxt_cost in node[now]:
            tmp = cost + nxt_cost

            if D[nxt] > tmp:
                D[nxt] = tmp
                heapq.heappush(q, [nxt, tmp])

    cnt = ans = 0
    for i in range(1, n + 1):
        if D[i] != inf:
            cnt += 1
            ans = max(ans, D[i])

    print(cnt, ans)