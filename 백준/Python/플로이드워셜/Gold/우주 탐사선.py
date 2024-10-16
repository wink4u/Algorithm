import sys
input = sys.stdin.readline

n, k = map(int, input().split())

planet = [list(map(int, input().split())) for _ in range(n)]

res = int(1e12)
visit = [0 for _ in range(n)]
visit[k] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            planet[i][j] = min(planet[i][j], planet[i][k] + planet[k][j])
print(planet)

def back(curr, cnt, total):
    global res
    if cnt == n:
        res = min(res, total)
        return

    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            back(i, cnt + 1, total + planet[curr][i])
            visit[i] = 0

back(k, 1, 0)
print(res)