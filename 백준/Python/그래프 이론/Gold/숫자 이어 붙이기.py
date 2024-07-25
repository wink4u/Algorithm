import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

MOD = 1000000007

N, Q = map(int, input().split())
value = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def find_path(start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))


for _ in range(Q):
    x, y = map(int, input().split())
    if x == y:
        print(value[x])
    else:
        path = find_path(x, y)
        result = ""
        for node in path:
            result += str(value[node])
        print(int(result) % MOD)
