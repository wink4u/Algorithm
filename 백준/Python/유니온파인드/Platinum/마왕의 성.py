import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
height_map = []
sort_by_height = defaultdict(list)
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        sort_by_height[tmp[j]].append((i, j))
    height_map.append(tmp)

tax = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 부모
parent = [[(-1, -1) for _ in range(m)] for _ in range(n)]
# 높이 체크
height = [[0 for _ in range(m)] for _ in range(n)]
# 정답배열
ans = [[0 for _ in range(m)] for _ in range(n)]


def find(x, y):
    if parent[x][y] == (-1, -1):
        return (x, y)
    parent[x][y] = find(*parent[x][y])
    return parent[x][y]


def union(p1, p2):
    p1 = find(*p1)
    p2 = find(*p2)

    if p1 == p2:
        return

    if height[p1[0]][p1[1]] < height[p2[0]][p2[1]]:
        p1, p2 = p2, p1

    parent[p2[0]][p2[1]] = p1

    if height[p1[0]][p1[1]] == height[p2[0]][p2[1]]:
        height[p1[0]][p1[1]] += 1

    tax[p1[0]][p1[1]] += tax[p2[0]][p2[1]]


for h in sorted(sort_by_height.keys()):
    coord_list = sort_by_height[h]

    for x, y in coord_list:
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and height_map[nx][ny] <= h:
                union((x, y), (nx, ny))

    for x, y in coord_list:
        px, py = find(x, y)
        ans[x][y] = tax[px][py]

for row in ans:
    print(" ".join(map(str, row)))
