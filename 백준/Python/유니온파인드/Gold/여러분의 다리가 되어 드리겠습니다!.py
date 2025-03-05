import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n + 1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


for _ in range(n - 2):
    a, b = map(int, input().split())
    union(a, b)

for i in range(2, n + 1):
    if find(1) != find(i):
        print(1, i)
        break