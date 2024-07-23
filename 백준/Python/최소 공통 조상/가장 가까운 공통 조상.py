import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    parent = [0] * (N + 1)
    d = [0] * (N + 1)
    root = [True] * (N + 1)

    def dfs(x, depth):
        d[x] = depth

        for y in graph[x]:
            parent[y] = x
            dfs(y, depth + 1)

    def LCA(a, b):
        while d[a] != d[b]:
            if d[a] > d[b]:
                a = parent[a]
            else:
                b = parent[b]

        while a != b:
            a = parent[a]
            b = parent[b]

        return a

    for _ in range(N - 1):
        a, b = map(int, input().split())
        root[b] = False
        graph[a].append(b)

    f_root = root[1:].index(True)
    dfs(f_root + 1, 0)
    a, b = map(int, input().split())
    print(LCA(a, b))
