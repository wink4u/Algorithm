import sys
input = sys.stdin.readline

n, t = map(int, input().split())
graph = [[1e9] * (n + 1) for _ in range(n + 1)]

for _ in range(t):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

s = int(input())

for _ in range(s):
    x, y = map(int, input().split())
    if graph[x][y] == 1e9 and graph[y][x] == 1e9:
        print(0)
    elif graph[x][y] == 1:
        print(-1)
    else:
        print(1)