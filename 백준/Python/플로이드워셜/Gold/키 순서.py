import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

ans = 0

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        cnt += graph[i][j] + graph[j][i]

    if cnt == n - 1:
        ans += 1

print(ans)