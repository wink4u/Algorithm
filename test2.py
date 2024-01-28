import sys
input = sys.stdin.readline

N = int(input())

new_boards = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# d가 0 이면 아래로 1이면 위로 2면 오른쪽 3면 왼쪽

result = 0

def check(boards, cnt, value):
    global result
    if cnt == 5:
        for i in range(len(boards)):
            result = max(result, max(boards[i]))
        return

    if value < result:
        return

    for d in range(4):
        if d == 0:
            for j in range(N):
                cursor = N - 1
                for i in range(N - 1, -1, -1):
                    if boards[i][j] != 0:
                        tmp = boards[i][j]
                        boards[i][j] = 0

                        if boards[cursor][j] == 0:
                            boards[cursor][j] = tmp

                        elif boards[cursor][j] == tmp:
                            boards[cursor][j] *= 2
                            cursor -= 1

                        else:
                            cursor -= 1
                            boards[cursor][j] = tmp

                    # value = max(value, boards[j][cursor])

        elif d == 1:
            for j in range(N):
                cursor = 0
                for i in range(N):
                    if boards[i][j] != 0:
                        tmp = boards[i][j]
                        boards[i][j] = 0

                        if boards[cursor][j] == 0:
                            boards[cursor][j] = tmp

                        elif boards[cursor][j] == tmp:
                            boards[cursor][j] *= 2
                            cursor += 1

                        else:
                            cursor += 1
                            boards[cursor][j] = tmp
                    # value = max(value, boards[j][cursor])
        elif d == 2:
            for i in range(N):
                cursor = N - 1
                for j in range(N - 1, -1, -1):

                    if boards[i][j] != 0:
                        tmp = boards[i][j]
                        boards[i][j] = 0

                        if boards[i][cursor] == 0:
                            boards[i][cursor] = tmp

                        elif boards[i][cursor] == tmp:
                            boards[i][cursor] *= 2
                            cursor -= 1
                        else:
                            cursor -= 1
                            boards[i][cursor] = tmp

                    # value = max(value, boards[j][cursor])

        else:
            for i in range(N):
                cursor = 0
                for j in range(1, N):
                    if boards[i][j] != 0:
                        temp = boards[i][j]
                        boards[i][j] = 0

                        if boards[i][cursor] == 0:
                            boards[i][cursor] = temp
                        elif boards[i][cursor] == temp:
                            boards[i][cursor] *= 2
                            cursor += 1
                        else:
                            cursor += 1
                            boards[i][cursor] = temp

                    # value = max(value, boards[j][cursor])

        # print(d)
        #
        # for i in range(len(boards)):
        #     print(boards[i])
        # print('----------------------------------')
        check(boards, cnt + 1, value)


check(new_boards, 0, 0)
print(result)