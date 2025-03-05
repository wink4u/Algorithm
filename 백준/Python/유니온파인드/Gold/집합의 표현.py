import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    pa = find(a)
    pb = find(b)

    if a < b:
        parent[pb] = pa
    else:
        parent[pb] = pa


for _ in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')