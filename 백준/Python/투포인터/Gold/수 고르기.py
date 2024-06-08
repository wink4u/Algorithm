import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
res = max(arr) - min(arr)
L, R = 0, 1
while L < R:
    if arr[R] - arr[L] < M:
        if R != N - 1:
            R += 1
        else:
            L += 1
    else:
        res = min(res, arr[R] - arr[L])
        L += 1
        if L == R and L != N - 1:
            R += 1



print(res)