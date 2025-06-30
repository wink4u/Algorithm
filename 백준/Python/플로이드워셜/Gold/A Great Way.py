import sys
input = sys.stdin.readline

n, r = map(int, input().split())
check = [[[1e11, 1] for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(r):
    # 시작거점, 도착거점, 기본요금, 1분당 추가요금, 걸리는 시간
    a, b, c, d, e = map(int, input().split())
    v = c if e <= 10 else c + (e - 10) * d

    if v < check[a][b][0]:
        check[a][b] = [v, 2]

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                if check[i][j][0] > check[i][k][0] + check[k][j][0]:
                    check[i][j][0] = check[i][k][0] + check[k][j][0]
                    check[i][j][1] = check[i][k][1] + check[k][j][1] - 1
                elif check[i][j][0] == check[i][k][0] + check[k][j][0]:
                    check[i][j][1] = min(check[i][j][1], check[i][k][1] + check[k][j][1] - 1)

res, cnt = check[1][n]
if res == 1e11:
    print('It is not a great way.')
else:
    print(res, cnt)