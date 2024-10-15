import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    graph[a][a] = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    cnt = 0
    for b in range(1, n + 1):
        if graph[a][b] == INF and graph[b][a] == INF:
            cnt += 1

    print(cnt)