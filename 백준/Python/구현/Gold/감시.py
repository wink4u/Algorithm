import sys
import copy
input = sys.stdin.readline


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dic = {2: [[0, 1], [2, 3]], 3: [[0, 3], [1, 3], [0, 2], [1, 2]],
        4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], 5: [[0, 1, 2, 3]]}


cctv = []
non_see = 0
visit = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j]:
            if board[i][j] != 6:
                visit[i][j] = 1
                cctv.append([i, j])
        else:
            non_see += 1


answer = n * m

def dfs(v, idx, total):
    global answer
    if idx == len(cctv):
        answer = min(answer, non_see - total)
        return

    for i in range(idx, len(cctv)):
        x, y = cctv[i]
        num = board[x][y]

        if num == 1:
            for d in range(4):
                sx, sy = x, y
                tmp = copy.deepcopy(v)
                cnt = 0
                while True:
                    nx, ny = sx + dx[d], sy + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] == 6:
                            break

                        if not tmp[nx][ny]:
                            tmp[nx][ny] = 1
                            cnt += 1

                        sx, sy = nx, ny
                    else:
                        break
                dfs(tmp, i + 1, total + cnt)
        else:
            cctv_arr = dic[num]
            for j in range(len(cctv_arr)):
                tmp = copy.deepcopy(v)
                cnt = 0
                for k in range(len(cctv_arr[j])):
                    d = cctv_arr[j][k]
                    sx, sy = x, y
                    while True:
                        nx, ny = sx + dx[d], sy + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if board[nx][ny] == 6:
                                break

                            if not tmp[nx][ny]:
                                tmp[nx][ny] = 1
                                cnt += 1

                            sx, sy = nx, ny
                        else:
                            break
                dfs(tmp, i + 1, total + cnt)

dfs(visit, 0, 0)

print(answer)