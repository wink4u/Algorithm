import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

N = int(input())

parent = [0] * (N + 1)
D = [0] * (N + 1)
C = [0] * (N + 1)

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    C[x] = True
    D[x] = depth

    for y in graph[x]:
        if C[y]:
            continue

        parent[y] = x
        dfs(y, depth + 1)

def lca(a, b):
    while D[a] != D[b]:
        if D[a] > D[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a

dfs(1, 0)

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))