import sys
input = sys.stdin.readline

n = int(input())
planet = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

node = []

for i in range(1, n):
    for j in range(i):
        node.append([planet[i][j], i, j])

node.sort()
res = 0
for cost, x, y in node:
    if find(x) != find(y):
        union(x, y)
        res += cost

print(res)
