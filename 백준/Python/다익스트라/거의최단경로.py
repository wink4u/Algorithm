import sys
import heapq
from collections import deque

input = sys.stdin.readline

inf = 1e9


def djkstra():
    distance = [inf] * (N + 1)
    distance[S] = 0
    q = []
    heapq.heappush(q, [0, S])

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for next_road, next_cost in rode[now]:
            cost = dist + next_cost

            if cost < distance[next_road]:
                if visit[now][next_road]: continue
                distance[next_road] = cost
                heapq.heappush(q, [cost, next_road])

    return distance

def bfs():
    q = deque()
    q.append(D)

    while q:
        current = q.popleft()

        if current == S:
            continue

        for post_rode, post_cost in inv_rode[current]:
            if distance[post_rode] + post_cost == distance[current] and not visit[post_rode][current]:
                visit[post_rode][current] = True
                q.append(post_rode)

while True:
    # 장소의 수, 도로의 수
    N, M = map(int, input().split())
    # 시작점 , 도착점
    if N == 0 and M == 0:
        break

    S, D = map(int, input().split())

    rode = [[] for _ in range(N)]
    inv_rode = [[] for _ in range(N)]
    visit = [[False for _ in range(N)] for _ in range(N)]

    for i in range(M):
        U, V, P = map(int, input().split())
        rode[U].append([V, P])
        inv_rode[V].append([U, P])

    distance = djkstra()
    bfs()
    distance = djkstra()

    if distance[D] == inf:
        print(-1)
    else:
        print(distance[D])


