import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = list(range(n))

enemy = defaultdict(list)

def find(a):
    if a == parent[a]:
        return a

    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa <= pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


for _ in range(m):
    t, p, q = input().split()

    p = int(p) - 1
    q = int(q) - 1

    if t == 'F':
        union(p, q)
    else:
        enemy[p].append(q)
        enemy[q].append(p)

def isenemy(a, b):
    for i in enemy[a]:
        for j in enemy[b]:
            if i == j:
                return True
    return False

for i in range(n - 1):
    for j in range(i + 1, n):
        if parent[i] != parent[j] and isenemy(i, j):
            union(i, j)

for i in range(n):
    find(i)

print(len(set(parent)))