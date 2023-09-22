import sys
import heapq

inf = 1e8

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

doro = [[] for _ in range(N + 1)]

for i in range(M):
    start, end = map(int, input().split())
    doro[start].append((end, 1))

D = [inf] * (N + 1)

def check(num):
    q = []
    D[num] = 0
    heapq.heappush(q, [0, num])

    while q:
        dist, now = heapq.heappop(q)

        if D[now] < dist:
            continue

        for i in doro[now]:
            cost = dist + i[1]

            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

    return D

check(X)

cnt = 0
for i in range(1, len(D)):
    if D[i] == K:
        print(i)
    else:
        cnt += 1

if cnt == N:
    print(-1)