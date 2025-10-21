import sys
import heapq
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
q = int(input())
arr = [list(map(int, input().split())) for _ in range(q)]

D = [1e12] * n
D[0] = 0

def djkstra():
    pq = []
    heapq.heappush(pq, [0, 0])

    while len(pq):
        dist, now = heapq.heappop(pq)

        if D[now] < dist:
            continue

        for nxt in range(n):
            if now == nxt:
                continue

            v = (now - nxt + n) % n
            w = A[v - 1]

            if w == 0:
                continue

            cost = dist + w
            if D[nxt] > cost:
                D[nxt] = cost
                heapq.heappush(pq, [cost, nxt])

djkstra()

for a, b in arr:
    v = (b - a + n) % n
    print(-1 if D[v] == 1e12 else D[v])
