import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


n, m = map(int, input().split())

boom = [0, 0, 0, 0]

board = [list(map(int, input().split())) for _ in range(n)]
command = []

for _ in range(m):
    command.append(list(map(int, input().split())))

sx, sy = (n + 1) // 2 - 1, (n + 1) // 2 - 1
board[sx][sy] = -1

def first():
    # 좌 하 우 상
    fx = [0, 1, 0, -1]
    fy = [-1, 0, 1, 0]

    # fx, fy를 통한 move_cnt 값
    move_cnt = 0
    # 움직일수있는 dir_cnt 값
    dir_cnt = 1
    # 그냥 이동한 값
    cnt = 0

    arr = []
    fd = 0
    s_x, s_y = sx, sy
    not_boom = []

    while True:
        n_fx, n_fy = s_x + fx[fd], s_y + fy[fd]
        if 0 <= n_fx < n and 0 <= n_fy < n:
            if board[n_fx][n_fy]:
                if arr:
                    if board[n_fx][n_fy] != arr[-1]:
                        if len(arr) >= 4:
                            boom[arr[-1]] += len(arr)
                            not_boom.append([0, 0])
                        else:
                            not_boom.append([len(arr), arr[0]])

                        arr = [board[n_fx][n_fy]]
                    else:
                        arr.append(board[n_fx][n_fy])
                else:
                    arr = [board[n_fx][n_fy]]

            cnt += 1
            s_x, s_y = n_fx, n_fy

            if cnt == dir_cnt:
                fd = (fd + 1) % 4
                move_cnt += 1
                cnt = 0
                if move_cnt == 2:
                    move_cnt = 0
                    dir_cnt += 1
        else:
            if len(arr) >= 4:
                boom[arr[-1]] += len(arr)
            else:
                if arr:
                    not_boom.append([len(arr), arr[0]])
            break

    res = []
    # print(boom)
    if not_boom:
        while True:
            # print(not_boom)
            tmp = []
            if len(not_boom) == 1:
                break

            flag = 0

            if [0, 0] in not_boom:
                while True:
                    if [0, 0] in not_boom:
                        idx = not_boom.index([0, 0])

                        l_idx, r_idx = idx - 1, idx + 1

                        if l_idx < 0 or r_idx >= len(not_boom):
                            not_boom[idx] = [-1, -1]
                        else:
                            if not_boom[l_idx][1] == not_boom[r_idx][1]:
                                not_boom[r_idx] = [not_boom[r_idx][0] + not_boom[l_idx][0], not_boom[r_idx][1]]
                                not_boom[l_idx] = [-1, -1]
                            not_boom[idx] = [-1, -1]
                        # print(not_boom)
                    else:
                        # print('here')
                        for i in range(len(not_boom)):
                            if not_boom[i][0] >= 4:
                                boom[not_boom[i][1]] += not_boom[i][0]
                                tmp.append([0, 0])
                                flag = 1
                            elif not_boom[i] != [-1, -1]:
                                tmp.append(not_boom[i])
                        break
            else:
                tmp.append(not_boom[0])
                idx = 1
                flag2 = 0
                while True:
                    if idx == len(not_boom):
                        break

                    if flag2:
                        tmp.append(not_boom[idx])
                        idx += 1
                    else:
                        t_c, t_n = tmp.pop()
                        if not_boom[idx][1] == t_n:
                            if not_boom[idx][0] + t_c >= 4:
                                boom[not_boom[idx][1]] += not_boom[idx][0] + t_c
                                flag = 1
                                flag2 = 1
                                tmp.append([0, 0])
                            else:
                                tmp.append([not_boom[idx][0] + t_c, t_n])
                        else:
                            tmp.append([t_c, t_n])
                            tmp.append(not_boom[idx])

                        idx += 1

            not_boom = tmp
            # print(not_boom, flag)
            if not flag:
                # print(boom)
                break
        # print('------------------------------------------------------------')
        for i in range(len(not_boom)):
            res.append(not_boom[i][0])
            res.append(not_boom[i][1])
        return res
    else:
        return []


def second(n_arr):
    new_board = [[0] * n for _ in range(n)]
    new_board[sx][sy] = -1

    fx = [0, 1, 0, -1]
    fy = [-1, 0, 1, 0]

    # fx, fy를 통한 move_cnt 값
    move_cnt = 0
    # 움직일수있는 dir_cnt 값
    dir_cnt = 1
    # 그냥 이동한 값
    cnt = 0

    fd = 0
    s_x, s_y = sx, sy

    len_arr = len(n_arr)
    idx = 0
    while True:
        n_fx, n_fy = s_x + fx[fd], s_y + fy[fd]
        if 0 <= n_fx < n and 0 <= n_fy < n:
            new_board[n_fx][n_fy] = n_arr[idx]
            idx += 1

            if idx == len_arr:
                break

            cnt += 1
            s_x, s_y = n_fx, n_fy

            if cnt == dir_cnt:
                fd = (fd + 1) % 4
                move_cnt += 1
                cnt = 0
                if move_cnt == 2:
                    move_cnt = 0
                    dir_cnt += 1
        else:
            break

    return new_board

for d, s in command:
    x, y = sx, sy
    for i in range(s):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny]:
                board[nx][ny] = 0
                x, y = nx, ny

    result = first()
    if result:
        board = second(result)
    else:
        break
    # pprint(board)

ans = 0

for i in range(1, 4):
    ans += boom[i] * i

print(ans)