import sys
input = sys.stdin.readline

N, M, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

def change(num, arr):
    for n in num:
        half_N = len(arr) // 2
        half_M = len(arr[0]) // 2
        if n == 1:
            z_arr = list(map(list, zip(*arr)))
            for i in range(len(z_arr)):
                z_arr[i].reverse()

            arr = list(map(list, zip(*z_arr)))
        elif n == 2:
            for i in range(len(arr)):
                arr[i].reverse()
        elif n == 3:
            tmp = [[0] * len(arr) for _ in range(len(arr[0]))]
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    tmp[j][len(arr) - i - 1] = arr[i][j]

            arr = tmp
        elif n == 4:
            tmp = [[0] * len(arr) for _ in range(len(arr[0]))]
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    tmp[len(arr[0]) - j - 1][i] = arr[i][j]
            arr = tmp
        elif n == 5:
            for i in range(half_N):
                for j in range(half_M):
                    tmp = arr[i][j]
                    arr[i][j] = arr[i + half_N][j]
                    arr[i + half_N][j] = arr[i + half_N][j + half_M]
                    arr[i + half_N][j + half_M] = arr[i][j + half_M]
                    arr[i][j + half_M] = tmp
        elif n == 6:
            for i in range(half_N):
                for j in range(half_M):
                    tmp = arr[i][j]
                    arr[i][j] = arr[i][j + half_M]
                    arr[i][j + half_M] = arr[i + half_N][j + half_M]
                    arr[i + half_N][j + half_M] = arr[i + half_N][j]
                    arr[i + half_N][j] = tmp

    return arr

res = change(command, board)

for i in range(len(res)):
    print(*res[i])