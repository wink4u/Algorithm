import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, k = map(int, input().split())

parent = list(range(n))
money = list(map(int, input().split()))

def trans_parent(p, c):
    for i in range(n):
        if parent[i] == p:
            parent[i] = c

def find(a):
    if a == parent[a]:
        return a

    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    pa = find(a)
    pb = find(b)

    if money[pa] < money[pb]:
        parent[pb] = pa
        if pb in parent:
            trans_parent(pb, pa)
    else:
        parent[pa] = pb
        if pa in parent:
            trans_parent(pa, pb)

for _ in range(m):
    a, b = map(int, input().split())

    if find(a - 1) != find(b - 1):
        union(a - 1, b - 1)

parent = list(set(parent))
flag = 0
total = k

for i in range(len(parent)):
    if total >= money[parent[i]]:
        total -= money[parent[i]]
    else:
        flag = 1
        break


if flag:
    print('Oh no')
else:
    print(k - total)