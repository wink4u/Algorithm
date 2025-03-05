import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n))

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


turn = 0
for _ in range(m):
    a, b = map(int, input().split())
    turn += 1

    if find(a) != find(b):
        union(a, b)
    else:
        break
else:
    turn = 0

print(turn)