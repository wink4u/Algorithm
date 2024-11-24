import sys
input = sys.stdin.readline

v, e = map(int, input().split())
inf = 1e12
node = [[inf] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    a, b, w = map(int, input().split())
    node[a][b] = w


for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            node[i][j] = min(node[i][j], node[i][k] + node[k][j])

ans = inf
for t in range(1, v + 1):
    ans = min(ans, node[t][t])

if ans == inf:
    print(-1)
else:
    print(ans)