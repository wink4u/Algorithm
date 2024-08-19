import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    arr[i] += arr[i - 1]

_max, cnt = 0, 0
for i in range(X, N + 1):
    if _max < arr[i] - arr[i - X]:
        _max = arr[i] - arr[i - X]
        cnt = 1
    elif _max == arr[i] - arr[i - X]:
        cnt += 1


if _max:
    print(_max)
    print(cnt)
else:
    print("SAD")