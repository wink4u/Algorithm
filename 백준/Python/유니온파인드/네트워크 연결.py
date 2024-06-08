import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(N + 1)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

res = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        res += c

print(res)