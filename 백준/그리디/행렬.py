import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A, B = [], []

for _ in range(n):
    A.append(list(map(int, input().strip())))

for _ in range(n):
    B.append(list(map(int, input().strip())))


def change_arr(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                A[i][j] = 0

cnt = 0
if (n < 3 or m < 3) and A != B:
    cnt = -1
else:
    for i in range(n - 2):
        for j in range(m - 2):
            if A[i][j] != B[i][j]:
                change_arr(i, j)
                cnt += 1

if cnt != -1 and A != B:
    cnt = -1

print(cnt)
