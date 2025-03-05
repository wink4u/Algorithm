import sys
input = sys.stdin.readline

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

t = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    cycle = set()

    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            cycle.add(parent[a])

        if parent[a] in cycle or parent[b] in cycle:
            cycle.add(parent[a])
            cycle.add(parent[b])

        union(a, b)

    for i in range(1, n + 1):
        find(i)

    s_parent = list(set(parent))
    _sum = sum([1 if i not in cycle else 0 for i in s_parent]) - 1

    if _sum == 0:
        print(f'Case {t}: No trees.')
    elif _sum == 1:
        print(f'Case {t}: There is one tree.')
    else:
        print(f'Case {t}: A forest of {_sum} trees.')
    t += 1