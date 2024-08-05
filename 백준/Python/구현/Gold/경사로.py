import sys
input = sys.stdin.readline

N, L = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
sero_board = list(map(list, zip(*board)))
res = 0

def check(arr):
    visit = [0] * (N)

    for i in range(N - 1):
        if arr[i] == arr[i + 1]:
            continue
        elif abs(arr[i] - arr[i + 1]) > 1:
            return False
        else:
            if arr[i] > arr[i + 1]:
                tmp = arr[i + 1]
                for j in range(i + 1, i + L + 1):
                    if 0 <= j < N:
                        if tmp != arr[j]:
                            return False
                        elif visit[j]:
                            return False

                        visit[j] = True
                    else:
                        return False
            else:
                tmp = arr[i]
                for j in range(i, i - L , -1):
                    if 0 <= j < N:
                        if tmp != arr[j]:
                            return False
                        elif visit[j]:
                            return False

                        visit[j] = True
                    else:
                        return False

    return True

for i in range(N):
    if check(board[i]):
        res += 1

for i in range(N):
    if check(sero_board[i]):
        res += 1

print(res)