import sys
from pprint import pprint
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

DP = [[0 for _ in range(N)] for _ in range(N)]
DP[0][1] = 1

print(house)
dx = [1, 0, 1]
dy = [0, 1, 1]

for i in range(N):
    for j in range(N):
        if DP[i][j]:
            for d in range(3):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < N and 0 <= nj < N and house[ni][nj] == 0:
                    DP[ni][nj] += 1
                    print(i, j, ni, nj)
                    for i in range(N):
                        print(DP[i])
                    print('----------')
print(DP[N - 1][N - 1])