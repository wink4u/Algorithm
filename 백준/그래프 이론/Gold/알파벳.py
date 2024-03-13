import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
alpha = []
for i in range(R):
    tmp = list(map(str, input().strip()))
    alpha.append(tmp)

res = 0

def check(x, y, cnt):
    global res
    res = max(res, cnt)

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < R and 0 <= ny < C and not visit[ord(alpha[nx][ny]) - 65]:
            visit[ord(alpha[nx][ny]) - 65] = 1
            check(nx, ny, cnt + 1)
            visit[ord(alpha[nx][ny]) - 65] = 0


visit = [0] * 26
visit[ord(alpha[0][0]) - 65] = 1
check(0, 0, 1)
print(res)