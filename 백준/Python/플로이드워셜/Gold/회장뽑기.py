import sys
input = sys.stdin.readline

INF = 1e11
N = int(input())
friend = [[INF] * (N + 1) for _ in range(N + 1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break

    friend[a][b] = 1
    friend[b][a] = 1

for i in range(1, N + 1):
    friend[i][i] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if friend[i][j] == 1 or friend[i][j] == 0: continue
            elif friend[i][j] > friend[i][k] + friend[k][j]:
                friend[i][j] = friend[i][k] + friend[k][j]

res = []
for i in range(1, N + 1):
    res.append(max(friend[i][1:]))

m = min(res)
print(m, res.count(m))
for i, v in enumerate(res):
    if v == m:
        print(i + 1, end = ' ')